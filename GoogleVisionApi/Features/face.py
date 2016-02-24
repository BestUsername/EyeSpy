from GoogleVisionApi.Features import Feature


class FaceFeature(Feature):

    def request_key(self):
        return 'FACE_DETECTION'

    def response_key(self):
        return 'faceAnnotations'

    def min_size(self):
        return 1600, 1200

    def parse_result_to_text(self, result):
        pass
