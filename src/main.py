import sys

from render.render import render
from board.loader.loader import load

path = sys.argv[2]

pattern = load(path)
output = render(pattern)

print(output)
