directions = [[-1, -1], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0]]


def get_graph_from_connections(connections):
    """
    This function formats connections array as graph
    :param connections:
    :return: set
    """
    i = 0
    graph = None

    for connection in connections:
        if i < len(connections) - 1:
            key = get_coord_as_string(connection)

            if graph is None:
                graph = {key: {get_coord_as_string(connections[i + 1])}}
            else:
                graph.update({key: {get_coord_as_string(connections[i + 1])}})
            i = i + 1

    return graph


def get_coord_as_string(coords):
    """
    This function returns a representation of coord as string.
    ex : [1,1] => 1,1
    :param coords:
    :return:
    """
    return ','.join(str(coord) for coord in coords)


def get_connections(begin, end, board, chain=None):
    """
    This function get all connections between stones in the board
    :param begin:
    :param end:
    :param board: array of coords
    :param chain: array of connections
    :return: connections: array
    """
    if chain is None:
        chain = [begin]

    for direction in directions:

        x = begin[0] + direction[0]
        y = begin[1] + direction[1]

        if board[x][y] == 1:
            chain.append([x, y])

            if [x, y] == end:
                break
            else:
                get_connections([x, y], end, board, chain)

    return chain
