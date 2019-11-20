from board.coord import get_x_index


def put_stone(coords, board):
    new_board = board[:]
    if coords is None:
        raise ValueError("Coordinates for the stone is incorrect. Please, pick a new one")

    line = get_x_index(coords[0])
    column = int(coords[1])

    if is_outside(board, line, column):
        raise ValueError("Stone can't be put outside the board")

    if is_already_taken(board, line, column):
        raise ValueError("A stone already exists at this position")

    new_board[column - 1][line - 1] = 1

    return new_board


def is_outside(board, line, column):
    """
    Check if the stone can be put inside the board
    """
    length = len(board)
    return length <= line or length <= column


def is_already_taken(board, line, column):
    """ Check if the place is already taken """
    return board[column][line] == 1
