from GoogleVisionApi.Features import Feature


class TextFeature(Feature):
    def request_key(self):
        return 'TEXT_DETECTION'

    def response_key(self):
        return 'textAnnotations'

    def min_size(self):
        return 1024, 768

    def parse_result_to_text(self, result):
        pass
