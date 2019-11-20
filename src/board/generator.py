def generate(size):
    """"
    Returns an empty board
    :parameter size int Size board. Classical size are 9, 11, 14 or 19
    :return board array Array representation of board
    """
    # return [[0] * size] * size
    return [[0 for i in range(size)] for j in range(size)]
