directions = [[-1, -1], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0]]


class Graph:
    connections = {}

    def __init__(self, connection):
        self.connections = connection


class Connection:
    point = None
    neighbors = {}

    def __init__(self, stone, board):
        self.point = point
        self.neighbors = neighbors
