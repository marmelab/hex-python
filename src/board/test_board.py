from board.board import put_stone, is_correct_position, is_already_taken_place


def test_can_put_a_stone_on_board():
    """ def put_stone(coords, pattern) """
    expected = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    actual = put_stone(('A', 1), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    assert expected == actual


def test_can_check_incorrect_position():
    """ def is_correct_position(length, line, column) """
    expected = False
    actual = is_correct_position(3, 4, 0)
    assert expected == actual


def test_can_check_correct_position():
    """ def is_correct_position(length, line, column) """
    expected = True
    actual = is_correct_position(3, 2, 0)
    assert expected == actual


def test_can_check_if_place_is_already_assigned():
    """ def is_already_taken_place(pattern, line, column) """
    expected = True
    actual = is_already_taken_place([[1, 0, 0], [0, 0, 0], [0, 0, 0]], 0, 0)
    assert expected == actual


def test_can_check_if_place_is_empty():
    """ def is_already_taken_place(pattern, line, column) """
    expected = False
    actual = is_already_taken_place([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0, 0)
    assert expected == actual
