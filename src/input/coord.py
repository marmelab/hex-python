import re
import string


def ask_coords(board):
    """
    :return:
    """
    code = input("Stone on : ")
    regex = re.match("^([a-zA-Z]{1})([1-9]{1}[0-9]{0,1})$", code)
    if regex is None:
        print("Your input seems incorrect. Please check it and retry.")
        return ask_coords(board)

    [x, y] = get_coords(regex)

    if board.is_outside(x, y):
        print("Stone can't be put outside the board")
        return ask_coords(board)

    if board.has_stone_at_coord(x, y):
        print("A stone already exists at this position")
        return ask_coords(board)

    return x, y


def get_x_index(letter):
    """
    The x index is the "line" part of the board. Because x coordinate is a letter, we need his position in the alphabet.
    To begin at the 1 index, we add 1 to list index.
    :param letter:
    :return:
    """
    return list(string.ascii_uppercase).index(letter.upper()) + 1


def get_coords(regex):
    """
    :param regex:
    :return:
    """
    coords = regex.groups()

    x = int(get_x_index(coords[0])) - 1
    y = int(coords[1]) - 1

    return x, y
