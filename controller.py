from go import *
from engine import Engine
from constants import *


IDENTITY = {'human': True, 'computer': False}


class Player(object):
    def __init__(self, color: Color, identity: str = None):
        """
        Initialization of a player object
        :param color: str
        """
        self.color: Color = color
        self.identity: str = identity

    def move(self, engine: Engine, coordinate: Vertex):
        """
        Move a stone to the board
        :param engine: Engine
        :param coordinate: str
        :return: None
        """
        player_move: Move = '{} {}'.format(self.color, coordinate)
        return engine.play(player_move)

    def count(self, board):
        pass

