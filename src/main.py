import sys

from render.render import render
from board.generator import generate
from game.game import start

path = sys.argv[2]

# Game initialization
board = generate(9)
output = render(board)

print(render(board))

# Throw the game
start(board)
