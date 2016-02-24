import base64
import tempfile

import httplib2
from PIL import Image

from apiclient.discovery import build
from oauth2client.client import GoogleCredentials

from GoogleVisionApi.Features.label import LabelFeature


class Client:
    API_DISCOVERY_FILE = 'https://vision.googleapis.com/$discovery/rest?version=v1'

    def __init__(self):
        self._http = httplib2.Http()
        self._credentials = GoogleCredentials.get_application_default().create_scoped(
            ['https://www.googleapis.com/auth/cloud-platform'])
        self._credentials.authorize(self._http)
        self._service = build('vision', 'v1', self._http, discoveryServiceUrl=Client.API_DISCOVERY_FILE)

    def _get_scaled_dimensions(self, original_width, original_height, features):
        width, height = (0, 0)
        for feature in features:
            max_width, max_height = feature.min_size()
            width = max(width, max_width)
            height = max(height, max_height)

        if width > original_width and height > original_height:

            ratio = original_width / original_height

            scale_h_for_w = width / ratio
            scale_w_for_h = height * ratio
            if abs(scale_h_for_w - height) > abs(scale_w_for_h - width):
                return scale_w_for_h, height
            else:
                return width, scale_h_for_w
        else:
            return original_width, original_height

    def _get_request_body_dict(self, filename, features=None, scale=False):
        if not features:
            features = [LabelFeature()]

        use_filename = filename

        if scale:
            # When features return image regions, scale the points from use_filename to filename size
            with Image.open(filename) as image:
                use_filename = tempfile.NamedTemporaryFile()
                original_width, original_height = image.size
                new_width, new_height = self._get_scaled_dimensions(original_width, original_height, features)
                if new_width != original_width or new_height != original_height:
                    image = image.resize(new_width, new_height)
                    image.save(use_filename)

        req_array = []
        for feature in features:
            req_array.append(feature.get_dict())

        with open(use_filename, 'rb') as image:
            image_content = base64.b64encode(image.read())

        return {
            'requests': [{
                'image': {
                    'content': image_content
                },
                'features': req_array
            }]
        }

    def find_features(self, filename, features):
        result = {}

        body_dict = self._get_request_body_dict(filename, features)
        service_request = self._service.images().annotate(body=body_dict)
        response = service_request.execute()
        # this class only makes one image request per api call, so just use index 0
        feature_annotations = response['responses'][0]

        if 'error' in feature_annotations:
            result['error'] = feature_annotations['error']['message']

        for feature in features:
            if feature.response_key() in feature_annotations:
                result[feature.request_key()] = feature.parse_result_to_text(feature_annotations[feature.response_key()])
            else:
                print('{} did not succeed'.format(feature.request_key()))

        return result

