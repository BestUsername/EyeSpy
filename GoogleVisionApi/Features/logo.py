from GoogleVisionApi.Features import Feature


class LogoFeature(Feature):
    def request_key(self):
        return 'LOGO_DETECTION'

    def response_key(self):
        return 'logoAnnotations'

    def parse_result_to_text(self, result):
        pass
