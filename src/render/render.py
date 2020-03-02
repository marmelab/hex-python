import math
import os
import string
from board.board import has_stone_at_coord


def render(board):
    """ This function returns a string containing the current state of the board """
    schema = ""
    headers = "  "

    reversed_alphabet = list(string.ascii_uppercase[::-1])
    size = len(board)

    x_range = int(math.sqrt(size))
    y_range = x_range

    line_number = 0
    for x in range(x_range):
        line_txt = ""
        headers += reversed_alphabet.pop() + " "
        line_txt += str(line_number + 1) + (' ' * (line_number + 1))

        for y in range(y_range):
            line_txt += "⬢ " if has_stone_at_coord(board, x, y) else "⬡ "

        schema += line_txt + "\n"
        line_number = line_number + 1

    return headers + "\n" + schema


def clear():
    """
    Clear the current output
    :return:
    """
    os.system('clear')


def display_board(board):
    """
    This function prints the board in the console.
    :param board:
    :return:
    """
    print(render(board))


def end_game(board):
    """
    :param board:
    :return:
    """
    print("You win the game ! \n" + (render(board)) + "Congratulations !")
