from abc import ABCMeta, abstractmethod


class Feature:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def request_key(self):
        pass

    def max_results(self):
        return 3

    def get_dict(self):
        return {
            'type': self.request_key(),
            'maxResults': self.max_results()
        }

    @abstractmethod
    def parse_result_to_text(self, result):
        pass

    @abstractmethod
    def response_key(self):
        pass

    def min_size(self):
        return 640, 480
