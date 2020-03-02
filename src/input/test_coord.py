from input.coord import get_coords, get_x_index, WrongInputException
import re

DEFAULT_REGEX = "^([a-zA-Z]{1})([1-9]{1}[0-9]{0,1})$"


def test_can_get_an_index_from_letter():
    """ def get_x_index(letter) """
    assert get_x_index('a') == 1


def test_can_get_an_index_from_letter_even_if_capitalize():
    """ def get_x_index(letter) """
    assert get_x_index('Z') == 26


def test_can_get_back_the_coords_by_match():
    """ def get_coords(matches) """
    actual = get_coords(re.match(DEFAULT_REGEX, "A1"))
    assert actual[0] == 0
    assert actual[1] == 0


def test_can_throw_exception_if_coord_is_incorrect():
    """ def get_coords(matches) """
    try:
        get_coords(re.match(DEFAULT_REGEX, "KL"))
        assert False
    except WrongInputException:
        assert True

    try:
        get_coords(re.match(DEFAULT_REGEX, "45"))
        assert False
    except WrongInputException:
        assert True

    try:
        get_coords(re.match(DEFAULT_REGEX, "5L8"))
        assert False
    except WrongInputException:
        assert True
