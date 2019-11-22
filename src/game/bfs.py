def bfs_paths(graph, start, goal):
    """"
    This function returns all possible path to a start node and a goal node
    Source : https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
    """
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    """"
    This function get the shortest path between start and goal node.
    Because first one path returned by bfs_paths is the shortest, this function only returns this path.
    Source : https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
    """
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None
