class Board:
    size: 0
    player1_stones: {}

    def has_stone_at_coord(self, x, y):
        """
        :param x:
        :param y:
        :return:
        """
        for stone in self.player1_stones:
            if stone.x == x and stone.y == y:
                return True

        return False

    def generate(self, size):
        """
        Returns an empty board
        :parameter size int Size board. Classical size are 9, 11, 14 or 19
        :return board Object
        """
        self.size = size
        self.player1_stones = set()

        return self

    def is_outside(self, x, y):
        """
        Check if the stone can be put inside the board
        :param x:
        :param y:
        :return:
        """
        return self.size <= x or self.size <= y

    def put_stone(self, stone):
        """
        :param stone:
        :return:
        """
        self.player1_stones.add(stone)


class Stone:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def as_string(self):
        """
        String representation of stone
        :return: str
        """
        return str(self.x) + ',' + str(self.y)
