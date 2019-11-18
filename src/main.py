class Board:

    grid = []

    def __init__(self):
        self.grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1]]

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


output = Board().render()
print(output)
