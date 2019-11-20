def render(board):
    """ This function returns a string containing the current state of the board """

    schema = ""
    size = len(board)

    i = 0
    for line in board:
        line_txt = ""
        for stone in line:
            line_txt += "⬡ " if stone == 0 else "⬢ "

        length = i + (size * 2) + 2
        schema += line_txt.__add__("\n").ljust(length)

        i = i + 1

    return schema
