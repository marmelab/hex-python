from game.bfs import bfs_paths, shortest_path

graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'C', 'E'}}


def test_can_get_all_path_for_a_node():
    """" bfs_paths(graph, start, goal) """
    expected = [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

    actual = list(bfs_paths(graph, 'A', 'F'))

    assert expected == actual


def test_can_only_get_the_shortest_path():
    """shortest_path(graph, start, goal) """
    expected = ['A', 'C', 'F']

    actual = list(shortest_path(graph, 'A', 'F'))

    assert expected == actual
