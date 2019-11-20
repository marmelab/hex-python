import json


def load(path):
    """ Load the board with JSON file path """
    with open(path) as json_file:
        return json.load(json_file)
