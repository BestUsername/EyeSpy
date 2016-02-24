from GoogleVisionApi.Features import Feature


class SafeSearchFeature(Feature):
    def request_key(self):
        return 'SAFE_SEARCH_DETECTION'

    def response_key(self):
        return 'safeSearchAnnotation'

    def parse_result_to_text(self, result):
        pass
