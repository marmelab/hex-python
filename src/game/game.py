from board.board import Board, Stone
from graph.bfs import shortest_path
from graph.graph import Graph
from input.coord import ask_coords
from render.render import display_board, end_game, clear

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
    graph = Graph()
    return board.generate(MINI_SIZE), graph


def start():
    """
    This function manage the game flow.
    :return:
    """
    board, graph = initialize()
    display_board(board)

    turn = 0
    while True:
        turn = turn + 1
        x, y = ask_coords(board)

        stone = Stone(x, y)
        board.put_stone(stone)

        graph.load_from_board(board)

        if shortest_path(graph, 'start', 'end') is None:
            clear()
            display_board(board)
        else:
            clear()
            end_game(board)


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
