from render.render import render


def test_can_render_a_state_of_the_board():
    """ def render(board) """
    actual = render([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1],
    ])

    expected = """⬡ ⬡ ⬡ ⬡ ⬡ 
 ⬡ ⬡ ⬡ ⬡ ⬡ 
  ⬡ ⬡ ⬡ ⬡ ⬡ 
   ⬡ ⬡ ⬡ ⬢ ⬢ 
    ⬡ ⬡ ⬡ ⬡ ⬢ 
     """

    assert expected == actual
