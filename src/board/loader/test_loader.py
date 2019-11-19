import json
import unittest
import os

from src.board.loader.loader import load


class TestLoader(unittest.TestCase):

    path = "assets/board_test.json"
    content = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 1, ], [0, 0, 0, 0, 1]]

    def setUp(self):

        with open(self.path, 'w') as outfile:
            json.dump(self.content, outfile)

    def tearDown(self):

        os.remove(self.path)

    def test_load(self):

        actual = load(self.path)
        expected = self.content

        self.assertEqual(expected, actual)
