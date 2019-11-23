from board.board import Stone

directions = [[-1, -1], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0]]


class Graph:
    connections = set()

    def load_from_board(self, board):
        """
        :param board:
        :return:
        """
        start_neighbors = set()
        start_neighbors.add('0,' + str(i) for i in range(board.size))

        start = Connection().load_with_data('start', start_neighbors)
        self.connections.add(start)

        for stone in board.player1_stones:
            connection = Connection().load_with_stone(stone, board)
            self.connections.add(connection)

        end_neighbors = set()
        end_neighbors.add(str(board.size) + ',' + str(i) for i in range(board.size))

        end = Connection().load_with_data('end', end_neighbors)
        self.connections.add(end)


class Connection:
    point = None
    neighbors = {}

    def __str__(self):
        return self.point + '->{' + ",".join(self.neighbors) + '}'

    def load_with_data(self, point, neighbors):
        self.point = point
        self.neighbors = neighbors

        return self

    def load_with_stone(self, stone, board):
        self.point = stone.as_string()
        self.neighbors = find_neighbors(stone, board)

        return self


def find_neighbors(stone, board):
    neighbors = set()
    for direction in directions:
        x = stone.x - direction[0]
        y = stone.y - direction[1]
        if board.has_stone_at_coord(x, y):
            neighbor = Stone(x, y).as_string()
            neighbors.add(neighbor)
    return neighbors
