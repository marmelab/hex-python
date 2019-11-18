import unittest

from src.main import Board


class TestMainTestCase(unittest.TestCase):

    def test_render(self):

        board = Board()
        actual = board.render()

        expected = """⬡ ⬡ ⬡ ⬡ ⬡ 
 ⬡ ⬡ ⬡ ⬡ ⬡ 
  ⬡ ⬡ ⬡ ⬡ ⬡ 
   ⬡ ⬡ ⬡ ⬢ ⬢ 
    ⬡ ⬡ ⬡ ⬡ ⬢ 
     """

        self.assertEqual(expected, actual)

