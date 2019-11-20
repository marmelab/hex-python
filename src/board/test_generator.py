from board.generator import generate


def test_can_generate_an_empty_board():
    """ def generate(size) """
    expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    actual = generate(3)
    assert expected == actual
