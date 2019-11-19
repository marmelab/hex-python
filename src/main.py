import json
import sys

class Board:

    grid = []

    def load(self, path):
        """ Load the board with JSON file path """
        with open(path) as json_file:
            self.grid = json.load(json_file)

    def render(self):
        """ This function returns a string containing the current state of the board """

        schema = ""
        size = len(self.grid)
        i = 0
        for line in self.grid:
            line_txt = ""
            for stone in line:
                line_txt += "⬡ " if stone == 0 else "⬢ "

            length = i + (size * 2) + 2
            schema += line_txt.__add__("\n").ljust(length)

            i = i + 1

        return schema


path = sys.argv[2]

board = Board()
board.load(path)
print(board.render())
