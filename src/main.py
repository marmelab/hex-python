import sys

from render.render import render
from board.generator import generate
from game.game import clear
from board.coord import get_coord
from board.board import put_stone

path = sys.argv[2]

# Game initialization
pattern = generate(9)
output = render(pattern)

still_in_game = True
print(render(pattern))

while still_in_game:

    position = input("Stone on : ")
    clear()
    print("You put a stone on " + position)

    coords = get_coord(position)

    try:
        pattern = put_stone(coords, pattern)
    except ValueError as err:
        print(format(err))

    print(render(pattern))
