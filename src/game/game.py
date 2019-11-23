from render.render import display_board, end_game, clear
from input.coord import ask_coords
from board.board import Board

MINI_SIZE = 5
DEFAULT_SIZE = 11
HARD_SIZE = 14


def initialize():
    """
    Game initialization
    Can be load with :
        path = sys.argv[2]
        board = board.load(path)
    :return:
    """
    board = Board()
    return board.generate(MINI_SIZE)


def start():
    """
    This function manage the game flow.
    :return:
    """
    board = initialize()
    turn = 0
    while True:

        turn = turn + 1

        clear()
        display_board(board)

        x, y = ask_coords(board)

        board.put_stone(x, y)


def must_be_checked(board, turn):
    """
    This function permits to determine if a process of board is needed
    Rules are :
        -   Need at least the size of the board to fill a path
        -   1st and last line must have a stone
    """


def is_won():
    """
    This function check if the game is over
    :return: boolean
    """

    return False
