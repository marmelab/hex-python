import sys

from render.render import render
from board.generator import generate
from game.game import clear
from board.coord import get_coord
from board.board import put_stone

path = sys.argv[2]

# Game initialization
board = generate(9)
output = render(board)

still_in_game = True
print(render(board))

while still_in_game:

    position = input("Stone on : ")
    clear()
    print("You put a stone on " + position)

    coords = get_coord(position)

    try:
        board = put_stone(coords, board)
    except ValueError as err:
        print(format(err))

    print(render(board))
