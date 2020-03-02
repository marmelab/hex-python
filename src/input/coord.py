import re
import string


class WrongInputException(Exception): pass


class OutOfLimitException(Exception): pass


def ask_coords():
    """
    :return: [x, y]
    """
    code = input("Stone on : ")
    matches = re.match("^([a-zA-Z]{1})([1-9]{1}[0-9]{0,1})$", code)

    return get_coords(matches)


def get_x_index(letter):
    """
    The x index is the "line" part of the board. Because x coordinate is a letter, we need his position in the alphabet.
    To begin at the 1 index, we add 1 to list index.
    :param letter:
    :return:
    """
    try:
        x_index = list(string.ascii_uppercase).index(letter.upper()) + 1
    except ValueError:
        raise OutOfLimitException

    return x_index


def get_coords(matches):
    """
    :param matches:
    :return:
    """
    if matches is None:
        raise WrongInputException()

    splitted_matches = matches.groups()

    x = int(get_x_index(splitted_matches[0])) - 1
    y = int(splitted_matches[1]) - 1

    return x, y
