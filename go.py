import numpy as np

BOARD_SIZE = (19, 19)


class Board(object):
    def __init__(self):
        self.size = BOARD_SIZE[0] * BOARD_SIZE[1]  # 19 * 19 board
        self.p_status = {'empty': 0b00, 'black': 0b01, 'white': 0b10, 'dummy': 0b11}
        self.p_symbol = ['.', 'X', 'O', '.']
        self.x_axis = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
                       'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18
                       }
        self.y_axis = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, '11': 10,
                       '12': 11, '13': 12, '14': 13, '15': 14, '16': 15, '17': 16, '18': 17, '19': 18
                       }

        self.reset()

        self.board = np.zeros(BOARD_SIZE, dtype=np.int8)

        self.captured_b = 0
        self.captured_w = 0

    def reset(self):
        self.board = np.zeros(BOARD_SIZE, dtype=np.int8)
        self.captured_b = 0
        self.captured_w = 0
        return

    def get_vertex(self, coordinate):
        # TODO what if a user wrongly keys in
        x = self.x_axis[coordinate[0].upper()]
        y = self.y_axis[coordinate[1]]
        return self.board[x][y]

    def set_vertex(self, coordinate, val):
        # TODO what if a user wrongly keys in
        x = self.y_axis[coordinate[1:]]
        y = self.x_axis[coordinate[0].upper()]
        if self.board[x][y] == 0 and val != 0:
            self.board[x][y] = val
        return


class Vertex(object):
    def __init__(self):
        self.stack = {}
        self.status = {'live': 0, 'seki': 1, 'independent': 2}
