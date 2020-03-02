from game.game import is_won, must_be_checked


# def test_can_detect_if_a_classic_game_is_won():
#     """ is_won(board) """
#     expected = True
#
#     board = [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
#
#     actual = is_won(board)
#
#     assert expected == actual
#
#
# def test_can_know_if_the_board_must_be_checked():
#     """ must_be_checked(board, turn) """
#     expected = True
#
#     board = [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
#
#     actual = must_be_checked(board, 5)
#
#     assert expected == actual
