import argparse

from GoogleVisionApi.Features.label import LabelFeature
from GoogleVisionApi.client import Client


def main(filename):
    '''Run a label request on a single image'''
    client = Client()
    print(client.find_features(filename, [LabelFeature()]))
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'image_file', help='The image you\'d like to label.')
    args = parser.parse_args()
    main(args.image_file)