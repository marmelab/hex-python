
import unittest

from src.board.generator.generator import generate

class TestGenerator(unittest.TestCase):

    def test_generate(self):

        expected = [[0,0,0],[0,0,0],[0,0,0]]
        actual = generate(3)
        self.assertEqual(expected, actual)
