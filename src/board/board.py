class Board:
    size: 0
    stones: {}

    # def load(self, path):
    #     """ Load the board with JSON file path """
    #     with open(path) as json_file:
    #
    #         grid = json.load(json_file)
    #         self.size = len(grid)
    #
    #         for stone in grid:

    def has_stone_at_coord(self, x, y):
        """
        :param x:
        :param y:
        :return:
        """
        for stone in self.stones:
            if stone.x == x and stone.y == y:
                print(x, y)
                return True

        return False

    def generate(self, size):
        """
        Returns an empty board
        :parameter size int Size board. Classical size are 9, 11, 14 or 19
        :return board Object
        """
        self.size = size
        self.stones = set()

        return self

    def is_outside(self, x, y):
        """
        Check if the stone can be put inside the board
        :param x:
        :param y:
        :return:
        """
        return self.size <= x or self.size <= y

    def put_stone(self, x, y):
        """
        :param x:
        :param y:
        :return:
        """
        stone = Stone(x, y)
        self.stones.add(stone)


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
