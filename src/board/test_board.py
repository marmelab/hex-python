from board.board import put_stone, is_outside, is_already_taken_place


def test_can_put_a_stone_on_board():
    """ def put_stone(coords, board) """
    expected = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    actual = put_stone(('A', 1), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    assert expected == actual


def test_can_check_is_coord_is_outside_the_board():
    """ def is_outside(length, line, column) """
    expected = True
    actual = is_outside(3, 3, 0)
    assert expected == actual

    actual = is_outside(9, 26, 1)
    assert expected == actual


def test_can_check_is_coord_is_inside_the_board():
    """ def is_outside(length, line, column) """
    expected = False
    actual = is_outside(3, 2, 1)
    assert expected == actual


def test_can_check_if_place_is_already_assigned():
    """ def is_already_taken_place(board, line, column) """
    expected = True
    actual = is_already_taken_place([[1, 0, 0], [0, 0, 0], [0, 0, 0]], 0, 0)
    assert expected == actual


def test_can_check_if_place_is_empty():
    """ def is_already_taken_place(board, line, column) """
    expected = False
    actual = is_already_taken_place([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0, 0)
    assert expected == actual
