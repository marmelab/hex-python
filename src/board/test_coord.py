from board.coord import get_coord, get_x_index


def test_can_get_an_index_from_letter():
    """ def get_x_index(letter) """
    assert get_x_index('a') == 1


def test_can_get_an_index_from_letter_even_if_capitalize():
    """ def get_x_index(letter) """
    assert get_x_index('Z') == 26


def test_can_check_if_format_of_coord_is_well_formatted():
    """ def check_coord(coord) """
    assert get_coord("A1")[0] == "A"
    assert get_coord("A1")[1] == "1"


def test_can_return_none_if_coord_is_incorrect():
    """ def check_coord(coord) """
    assert get_coord("KL") is None
    assert get_coord("45") is None
    assert get_coord("5L8") is None
