from board.board import put_stone, is_outside, is_already_taken


def test_can_put_a_stone_on_board():
    """ def put_stone(coords, board) """
    expected = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    actual = put_stone(('A', 1), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    assert expected == actual


def test_can_check_is_coord_is_outside_the_board():
    """ def is_outside(length, line, column) """
    expected = True
    actual = is_outside([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 3, 0)
    assert expected == actual

    actual = is_outside([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 26, 1)
    assert expected == actual


def test_can_check_is_coord_is_inside_the_board():
    """ def is_outside(length, line, column) """
    expected = False
    actual = is_outside([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 2, 1)
    assert expected == actual

    actual = is_outside([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 2, 2)
    assert expected == actual


def test_can_check_if_place_is_already_assigned():
    """ def is_already_taken(board, line, column) """
    expected = True
    actual = is_already_taken([[1, 0, 0], [0, 0, 0], [0, 0, 0]], 0, 0)
    assert expected == actual


def test_can_check_if_place_is_empty():
    """ def is_already_taken(board, line, column) """
    expected = False
    actual = is_already_taken([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0, 0)
    assert expected == actual
