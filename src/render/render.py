import os
import string


def render(board):
    """ This function returns a string containing the current state of the board """
    schema = ""
    headers = "  "
    alphabet = list(string.ascii_uppercase)

    alphabet.reverse()

    x = y = 0

    empty_grid = [[0 for i in range(board.size)] for j in range(board.size)]

    for slot in empty_grid:

        line_txt = ""
        headers += alphabet.pop() + " "
        line_txt += str(y + 1) + (' ' * (y + 1))

        for stone in slot:
            line_txt += "⬢ " if board.has_stone_at_coord(x, y) else "⬡ "
            x = x + 1

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
    clear()
    print("You win the game ! \n" + (render(board)) + "Congratulations !")
