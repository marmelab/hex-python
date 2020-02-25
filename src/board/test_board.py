import json
import os

from board.board import put_stone, is_outside, is_already_taken, Board

path = "assets/board_test.json"
content = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 1, ], [0, 0, 0, 0, 1]]


def setup_module():
    with open(path, 'w') as outfile:
        json.dump(content, outfile)


def teardown_module():
    os.remove(path)


def test_can_load_a_json_file_of_coordinates():
    """" def load(path) """
    actual = Board.load(path).grid
    expected = content

    assert expected == actual


def test_can_generate_an_empty_board():
    """ def generate(size) """
    expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    actual = Board.generate(3).grid
    assert expected == actual


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
