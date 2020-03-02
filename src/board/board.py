class IsOutsideException(Exception):
    pass


class HasAlreadyAStoneException(Exception):
    pass


class IllegalStoneMove(Exception):
    pass


NO_PLAYER_VALUE = 0
PLAYER1_VALUE = 1


def is_valid_move(board, x, y):
    """
    :param board:
    :param x:
    :param y:
    :return:
    """
    if is_outside(board, x, y):
        raise IsOutsideException()

    if has_stone_at_coord(board, x, y):
        raise HasAlreadyAStoneException()

    return True


def generate(size):
    """
    Returns an empty board. Player is set to 0 for each case.
    :parameter size int Size board. Classical size are 9, 11, 14 or 19
    :return board
    """
    board = list()
    for x in range(size):
        for y in range(size):
            board.append([x, y, NO_PLAYER_VALUE])

    return board


def is_outside(board, x, y):
    """
    :param board:
    :param x:
    :param y:
    :return: boolean
    """
    return not is_inside(board, x, y)


def is_inside(board, x, y):
    """
    Check if the stone is inside the board
    :param board:
    :param x:
    :param y:
    :return: boolean
    """
    limit = len(board) - 1

    return 0 <= x <= limit and 0 <= y <= limit


def has_stone_at_coord(board, x, y):
    """
    Checks if a stone is already presents on asked position.
    :param board:
    :param x:
    :param y:
    :return:
    """
    for stone in board:
        if stone[0] == x and stone[1] == y and stone[2] != NO_PLAYER_VALUE:
            return True

    return False


def put_stone(board, x, y):
    """
    :param board:
    :param x:
    :param y:
    :return:
    """
    updated_board = board
    try:
        index_to_update = board.index([x, y, NO_PLAYER_VALUE])
        board[index_to_update] = [x, y, PLAYER1_VALUE]
    except ValueError:
        raise IllegalStoneMove()

    return updated_board


class Stone:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def as_string(self):
        """
        String representation of stone
        :return: str
        """
        return str(self.x) + ',' + str(self.y)
