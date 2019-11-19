import unittest

from src.render.render import render

class TestLoader(unittest.TestCase):

    def test_render(self):
        pattern = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1],
        ]

        actual = render(pattern)

        expected = """⬡ ⬡ ⬡ ⬡ ⬡ 
 ⬡ ⬡ ⬡ ⬡ ⬡ 
  ⬡ ⬡ ⬡ ⬡ ⬡ 
   ⬡ ⬡ ⬡ ⬢ ⬢ 
    ⬡ ⬡ ⬡ ⬡ ⬢ 
     """

        self.assertEqual(expected, actual)
