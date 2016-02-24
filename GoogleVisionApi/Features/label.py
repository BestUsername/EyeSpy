from GoogleVisionApi.Features import Feature


class LabelFeature(Feature):
    def request_key(self):
        return 'LABEL_DETECTION'

    def response_key(self):
        return 'labelAnnotations'

    def parse_result_to_text(self, result):
        text_array = []
        for entity in result:
            text_array.append('{} ({:.0%})'.format(entity['description'], entity['score']))
        return ', '.join(text_array)
