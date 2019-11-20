from render.render import render


def test_can_render_a_state_of_the_board():
    """ def render(board) """
    actual = render([
        [0, 0, 0, ],
        [0, 0, 0, ],
        [0, 0, 0, ]
    ])

    expected = """  A B C 
1 ⬡ ⬡ ⬡ 
2  ⬡ ⬡ ⬡ 
3   ⬡ ⬡ ⬡ 
"""

    print(actual)
    assert expected == actual
