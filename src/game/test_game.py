from game.game import game_winned, must_be_checked


def test_can_detect_if_a_classic_game_is_won():
    """ game_winned(board) """
    expected = True

    board = [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]

    actual = game_winned(board)

    assert expected == actual


def test_can_know_if_the_board_must_be_checked():
    """ must_be_checked(board, turn) """
    expected = True

    board = [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]

    actual = must_be_checked(board, 5)

    assert expected == actual
