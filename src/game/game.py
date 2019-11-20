import os
from render.coord import get_coord
from board.board import put_stone
from render.render import render


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

        if can_be_checked(board, turn) and game_winned(board):
            print("You win the game !")
            break


def can_be_checked(board, turn):
    """
    This function permits to determine if a process of board is needed
    Rules are :
        -   Need at least the size of the board to fill a path
        -   1st and last line must have a stone
    """
    length = len(board)
    last_index = length - 1

    return length < turn and board[0].count(1) > 0 and board[last_index].count(1) > 0


def game_winned(board):
    """ This function check if the game is over """
    winned = False



    return winned


def clear():
    os.system('clear')
