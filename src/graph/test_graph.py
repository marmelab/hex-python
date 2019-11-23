from game.graph import get_connections, get_graph_from_connections


def test_can_get_all_connections_between_a_begin_stone_and_end_one():
    """def get_connections(begin, end, board)"""
    content = [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
    expected = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]
    actual = get_connections([0, 0], [4, 0], content)

    assert expected == actual


def test_can_get_a_graph_from_connection_array():
    """def get_graph_from_connections(connections)"""
    connections = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]
    expected = {
        '0,0': {'1,0'},
        '1,0': {'2,0'},
        '2,0': {'3,0'},
        '3,0': {'4,0'},
    }

    actual = get_graph_from_connections(connections)

    assert expected == actual
