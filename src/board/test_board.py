import json
import os

from board.board import is_outside, is_inside, generate, put_stone, has_stone_at_coord

path = "assets/board_test.json"
content = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 1, ], [0, 0, 0, 0, 1]]


def setup_module():
    with open(path, 'w') as outfile:
        json.dump(content, outfile)


def teardown_module():
    os.remove(path)


def test_can_check_is_coord_is_outside_the_board():
    """ def is_outside(length, line, column) """
    assert is_outside([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 3, 0) is True
    assert is_outside([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 26, 1) is True
    assert is_outside([[0, 0, 0], [0, 0, 0], [0, 0, 0]], -1, 1) is True
    assert is_outside([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 2, -1) is True


def test_can_check_is_coord_is_inside_the_board():
    """ def is_outside(length, line, column) """
    assert is_inside([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 2, 1) is True
    assert is_inside([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 2, 2) is True


def test_can_generate_an_empty_board():
    """ def generate(size) """
    assert [[0, 0, 0], [0, 1, 0], [0, 2, 0],
            [1, 0, 0], [1, 1, 0], [1, 2, 0],
            [2, 0, 0], [2, 1, 0], [2, 2, 0]] == generate(3)


def test_can_put_a_stone_on_board():
    """ def put_stone(board, x, y) """
    assert [[0, 0, 1]] == put_stone([[0, 0, 0]], 0, 0)


def test_can_check_if_place_is_already_assigned():
    """ def has_stone_at_coord(board, x, y) """
    assert has_stone_at_coord([[0, 0, 1], [0, 0, 0], [0, 0, 0]], 0, 0) is True


def test_can_check_if_place_is_empty():
    """ def has_stone_at_coord(board, x, y) """
    assert has_stone_at_coord([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0, 0) is False
