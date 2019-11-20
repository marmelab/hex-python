import json
import os

from board.loader import load

path = "assets/board_test.json"
content = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 1, ], [0, 0, 0, 0, 1]]


def setup_module():
    with open(path, 'w') as outfile:
        json.dump(content, outfile)


def teardown_module():
    os.remove(path)


def test_can_load_a_json_file_of_coordinates():
    """" def load(path) """
    actual = load(path)
    expected = content

    assert expected == actual
