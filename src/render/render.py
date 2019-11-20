import string


def render(board):
    """ This function returns a string containing the current state of the board """

    schema = ""
    headers = "  "
    size = len(board)
    alphabet = list(string.ascii_uppercase)

    alphabet.reverse()

    i = 0
    for line in board:
        line_txt = ""
        headers += alphabet.pop().__add__(" ")

        line_txt += str(i + 1).__add__(' ' * (i + 1))
        for stone in line:
            line_txt += "⬡ " if stone == 0 else "⬢ "

        schema += line_txt.__add__("\n")

        i = i + 1

    return headers.__add__("\n") + schema
