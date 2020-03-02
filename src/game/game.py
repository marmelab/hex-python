from board.board import generate, put_stone, is_valid_move, HasAlreadyAStoneException, IsOutsideException
from graph.bfs import shortest_path
from input.coord import *
from render.render import display_board, end_game, clear

MINI_SIZE = 5
DEFAULT_SIZE = 11
HARD_SIZE = 14


def start():
    """
    This function manage the game flow.
    :return:
    """
    board = generate(MINI_SIZE)
    player1_stones = set()
    display_board(board)

    turn = 0
    while True:

        try:
            x, y = ask_coords()
            is_valid_move(board, x, y)

        except WrongInputException:
            print("Your input seems incorrect. Please check it and retry.")
            continue

        except IsOutsideException:
            print("Stone can't be put outside the board")
            continue

        except HasAlreadyAStoneException:
            print("A stone already exists at this position")
            continue

        turn = turn + 1
        put_stone(board, x, y)
    #
    #     graph.load_from_board(board)
    #
    #     if shortest_path(graph, 'start', 'end') is None:
    #         clear()
        display_board(board)
    #     else:
    #         clear()
    #         end_game(board)


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
