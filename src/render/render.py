import os
import string


def render(board):
    """ This function returns a string containing the current state of the board """
    schema = ""
    headers = "  "

    alphabet = list(string.ascii_uppercase)
    alphabet.reverse()

    y = 0

    empty_grid = [[[i, j] for i in range(board.size)] for j in range(board.size)]

    for line in empty_grid:
        line_txt = ""
        headers += alphabet.pop() + " "
        line_txt += str(y + 1) + (' ' * (y + 1))

        for slot in line:
            line_txt += "⬢ " if board.has_stone_at_coord(slot[0], slot[1]) else "⬡ "

        schema += line_txt + "\n"
        y = y + 1

    return headers + "\n" + schema


def clear():
    """
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
