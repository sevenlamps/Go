from go import Board


IDENTITY = {'human': True, 'computer': False}


class Player(object):
    def __init__(self, color, identity):
        """
        Initialization of a player object
        :param color: str
        """
        self.color = color
        self.identity = identity

    def move(self, board, coordinate):
        """
        Move a stone to the board
        :param board: Class
        :param coordinate: str
        :return: None
        """
        value = board.p_status[self.color]
        board.set(coordinate, value)
        return

    def count(self, board):
        pass

