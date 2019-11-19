import sys

from render.render import render
from board.generator.generator import generate

path = sys.argv[2]

board = generate(9)
output = render(board)

print(output)
