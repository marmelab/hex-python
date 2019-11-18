import json
import unittest
import os

from src.main import Board


class TestMainTestCase(unittest.TestCase):

    path = "assets/board_test.json"
    content = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 1, ], [0, 0, 0, 0, 1]]

    def setUp(self):

        with open(self.path, 'w') as outfile:
            json.dump(self.content, outfile)

    def tearDown(self):

        os.remove(self.path)

    def test_load(self):

        board = Board()
        board.load(self.path)

        self.assertEqual(board.grid, self.content)

    def test_render(self):
        board = Board()
        board.load(self.path)
        actual = board.render()

        expected = """⬡ ⬡ ⬡ ⬡ ⬡ 
 ⬡ ⬡ ⬡ ⬡ ⬡ 
  ⬡ ⬡ ⬡ ⬡ ⬡ 
   ⬡ ⬡ ⬡ ⬢ ⬢ 
    ⬡ ⬡ ⬡ ⬡ ⬢ 
     """

        self.assertEqual(expected, actual)
