from GoogleVisionApi.Features import Feature


class LandmarkFeature(Feature):
    def request_key(self):
        return 'LANDMARK_DETECTION'

    def response_key(self):
        return 'landmarkAnnotations'

    def parse_result_to_text(self, result):
        pass
