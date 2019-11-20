from board.coord import get_x_index


def put_stone(coords, pattern):
    """ Put a stone on the coords provided."""

    if coords is None:
        raise ValueError("Coordinates for the stone is incorrect. Please, pick a new one")

    line = get_x_index(coords[0]) - 1
    column = int(coords[1]) - 1

    lenght = len(pattern)

    if is_correct_position(lenght, line, column):
        raise ValueError("Stone can't be put outside the board")

    if is_already_taken_place(pattern, line, column):
        raise ValueError("A stone already exists at this position")

    pattern[column][line] = 1

    return pattern


def is_correct_position(length, line, column):
    """ Check if the stone can be put inside the board """

    return length > line & length > column


def is_already_taken_place(pattern, line, column):
    """ Check if the place is already taken """

    return pattern[column][line] == 1
