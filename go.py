import numpy as np
from typing import Dict, Tuple, List, NewType
from constants import *
from error import *
from collections import deque


BOARD_LENGTH = 19
BOARD_SIZE = (BOARD_LENGTH, BOARD_LENGTH)
STONE_STATUS = {'live': 0, 'seki': 1, 'independent': 2}
STONE_SYMBOL = {0: '.', 1: 'X', -1: 'O'}
COLOR = {'empty': 0, 'black': 1, 'white': -1}

Y_AXIS = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
          'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18
          }

X_AXIS = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, '11': 10,
          '12': 11, '13': 12, '14': 13, '15': 14, '16': 15, '17': 16, '18': 17, '19': 18
          }
PASS = (-1, -1)


Color = NewType('Color', str)
# TODO color type should be well defined, take string as input, and int output
Vertex = NewType('Vertex', str)
Move = NewType('Move', str)


class Point(NamedTuple):
    x: int
    y: int


class Chain(NamedTuple):
    stones: Set[Point]
    liberties: Set[Point]

    def in_atari(self):
        return len(self.liberties) == 1


class Board(object):
    def __init__(self):
        self.size: uint = BOARD_SIZE[0] * BOARD_SIZE[1]  # 19 * 19 board
        self.board: np.ndarray = np.zeros(BOARD_SIZE, dtype=uint)
        self.ko_point: Set[Point] = set()
        self.captured_b: int = 0
        self.captured_w: int = 0

    def get_color(self, p: Point) -> int:
        # TODO what if a user wrongly keys in
        return self.board[p.x][p.y]

    def set_color(self, color_val: int, p: Point):
        # TODO what if a user wrongly keys in
        self.board[p.x][p.y] = color_val
        return

    def update_captured(self, color_val: int, number_of_stones: int):
        if color_val == COLOR['black']:
            self.captured_b += number_of_stones
        elif color_val == COLOR['white']:
            self.captured_w += number_of_stones

