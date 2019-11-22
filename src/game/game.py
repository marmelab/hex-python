import os

from render.coord import get_coord
from board.board import put_stone
from render.render import render
from game.graph import get_connections, get_graph_from_connections, get_coord_as_string
from game.bfs import shortest_path


def start(board):
    """ This function manage the game flow"""
    turn = 0
    while True:

        turn = turn + 1

        position = input("Stone on : ")
        clear()
        print("You put a stone on " + position)

        coords = get_coord(position)

        try:
            board = put_stone(coords, board)
        except ValueError as err:
            print(format(err))

        print(render(board))

        if must_be_checked(board, turn) and game_winned(board):
            clear()
            print("You win the game ! \n".__add__(render(board)).__add__("Congratulations !"))
            break


def must_be_checked(board, turn):
    """
    This function permits to determine if a process of board is needed
    Rules are :
        -   Need at least the size of the board to fill a path
        -   1st and last line must have a stone
    """
    has_enough_stones = len(board) - 1 <= turn

    try:
        top = 1 in board[0]
        bottom = 1 in board[-1]
    except ValueError:
        pass
        return False

    return has_enough_stones and bottom and top


def game_winned(board):
    """
    This function check if the game is over
    :param board: array of coords
    :return: boolean
    """
    first_stones = [[0, stone] for stone in [board[0].index(1)]]
    last_stones = [[len(board) - 1, stone] for stone in [board[-1].index(1)]]

    for begin in first_stones:
        for end in last_stones:
            connections = get_connections(begin, end, board)
            graph = get_graph_from_connections(connections)

            chained = shortest_path(graph, get_coord_as_string(begin), get_coord_as_string(end))

            if chained is not None:
                return True

    return False


def clear():
    os.system('clear')
