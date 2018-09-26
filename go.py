import numpy as np
from typing import Dict, Tuple, List, NewType
from constants import *


BOARD_SIZE = (19, 19)
STONE_STATUS = {'live': 0, 'seki': 1, 'independent': 2}
STONE_SYMBOL = ['.', 'X', 'O', '.']
COLOR = {'empty': 0b00, 'black': 0b01, 'white': 0b10, 'dummy': 0b11}

Y_AXIS = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
          'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18
          }

X_AXIS = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, '11': 10,
          '12': 11, '13': 12, '14': 13, '15': 14, '16': 15, '17': 16, '18': 17, '19': 18
          }
PASS = (-1, -1)


class Board(object):
    def __init__(self):
        self.size: uint = BOARD_SIZE[0] * BOARD_SIZE[1]  # 19 * 19 board
        # self.p_status: dict = {'empty': 0b00, 'black': 0b01, 'white': 0b10, 'dummy': 0b11}
        # self.p_symbol: list = ['.', 'X', 'O', '.']

        self.board: np.ndarray = np.zeros(BOARD_SIZE, dtype=uint)

        self.captured_b: uint
        self.captured_w = uint

    def get(self, x: int, y: int) -> int:
        # TODO what if a user wrongly keys in
        return self.board[x][y]

    def set(self, color: int, coordinate: tuple):
        # TODO what if a user wrongly keys in
        if color != COLOR['empty'] and color != COLOR['dummy']:
            x = coordinate[0]
            y = coordinate[1]
            if self.board[x][y] == 0 and color != 0:
                self.board[x][y] = color
        return


# class Color(object):
#     def __init__(self, color: str):
#         self._color: str = color
#
#     def get(self) -> int:
#         return COLOR[self._color.upper()]


# class Vertex(object):
#     def __init__(self, coordinate: str):
#         self._coordinate: str = coordinate
#         self.status: int
#
#     def get(self) -> tuple:
#         if self._coordinate == 'pass':
#             return PASS
#         else:
#             x = X_AXIS[self._coordinate[0].upper()]
#             y = Y_AXIS[self._coordinate[1]]
#             return x, y


# class Move(object):
#     def __init__(self, move: str):
#         self._color = Color(move.split())
#         self._vertex = vertex
#
#     def get(self) -> tuple:
#         if self._vertex.get() == PASS:
#             return COLOR['empty'], PASS
#         else:
#             return self._color.get(), self._vertex.get()
