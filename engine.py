import logging
import numpy as np
from go import *
import threading
from constants import *
from error import *
from rule import *
import sgf



PROTOCOL_VERSION = 2
NAME = 'PyGo'
VERSION = '0.1'


class Engine(object):
    def __init__(self, move_stack: List[Move], komi: float, time_settings: int):
        """
        Initialization of new engine
        :param move_stack: vertex*[] vertices of move
        :param komi:
        :param time_settings:
        """
        self.go: Board = Board()
        self.default_board_size: tuple = BOARD_SIZE
        self.move_stack: List[Move] = move_stack
        self.komi: float = komi
        self.time_settings: int = time_settings
        self.commands: list = []

    # ###################################### Administrative Commands ###################################################
    @staticmethod
    def protocol_version() -> int:
        """
        For gtp specification 2.
        :return: int version number - Version of the GTP Protocol
        """
        return PROTOCOL_VERSION

    @staticmethod
    def name() -> str:
        """
        E.g. “GNU Go”, “GoLois”, “Many Faces of Go”. The name does
        not include any version information, which is
        provided by the version command.
        :return: string* name - Name of the engine
        """
        return NAME

    @staticmethod
    def version() -> str:
        """
        E.g. “3.1.33”, “10.5”. Engines without a sense of version
        number should return the empty string.
        :return: string* version - Version of the engine
        """
        return VERSION

    def known_command(self, command_name) -> bool:
        """
        The protocol makes no distinction between unknown commands
        and known but unimplemented ones. Do not declare
        a command as known if it is known not to work.
        :param command_name: string command name - Name of a command
        :return: boolean known - “true” if the command is known by
        the engine, “false” otherwise
        """
        return True if command_name in self.commands else False

    def list_commands(self):
        """
        Include all known commands, including required ones and
        private extensions.
        :return: string& commands - List of commands, one per row
        """
        for command in self.commands:
            print(command)
        return

    @staticmethod
    def quit():
        """
        The session is terminated and the connection is closed.
        :return: None
        """
        # TODO kill connection, currently not useful
        quit(0)
        return
    # ###################################### End of Administrative Commands ############################################

    # ###################################### Setup Commands ############################################################
    def set_boardsize(self, size):
        """
        Originally name in gtp2-spec: boardsize
        In GTP version 1 this command also did the work of
        clear board. This may or may not be true for implementations
        of GTP version 2. Thus the controller must
        call clear board explicitly. Even if the new board size is
        the same as the old one, the board configuration becomes
        arbitrary.
        :param size: int size - New size of the board.
        :return: none
        """
        # TODO currently not useful
        return

    def clear_board(self):
        """

        :return: None
        """
        self.go.board = np.zeros(BOARD_SIZE, dtype=uint)
        self.go.captured_b = 0
        self.go.captured_w = 0
        return

    def set_komi(self, new_komi: float):
        """
        Originally name in gtp2-spec: komi
        The engine must accept the komi even if it should be ridiculous.
        :param new_komi: float new komi - New value of komi.
        :return:
        """
        self.komi = new_komi
        return

    def fixed_handicap(self, number_of_stones):
        """
        This command is only valid if the board is empty. See
        section 4.1.1 for valid number of handicap stones. The
        handicap stones are not included in the move history.
        :param number_of_stones: int number of stones - Number of handicap stones.
        :return:vertex* vertices - A list of the vertices where handicap
        stones have been placed.
        """
        # TODO currently not useful
        return

    def place_free_handicap(self, number_of_stones):
        """
        This command is only valid if the board is empty. The engine
        may place fewer than the requested number of stones
        on the board under certain circumstances, as discussed
        in section 4.1.2. The controller can check this by counting
        the number of vertices in the response. The handicap
        stones are not included in the move history. Vertices must
        not be repeated or include “pass”.
        :param number_of_stones:
        :return:vertex* vertices - A list of the vertices where handicap
        stones have been placed.
        """
        # TODO currently not useful
        return

    def set_free_handicap(self, vertices):
        """
        This command is only valid if the board is empty. The
        list must have at least two elements and no more than
        the number of board vertices minus one. The engine must
        accept the handicap placement. The handicap stones are
        not included in the move history. Vertices must not be
        repeated or include “pass”.
        :param vertices: vertex* vertices - A list of vertices where handicap
        stones should be placed on the board.
        :return: None
        """
        # TODO currently not useful
        return
    # ###################################### End of Setup Commands #####################################################

    # ###################################### Core Play Commands ########################################################
    def play(self, move: Move):
        """
        Consecutive moves of the same color are not considered
        illegal from the protocol point of view.
        :param move:move move - Color and vertex of the move
        :return:None
        """
        # TODO  The number of captured stones is updated if needed and the move is added to the move history
        color, vertex = move.split()
        if vertex.lower() == 'pass':
            return 0
        if vertex.lower() == 'resign':
            # TODO update game status, show the game result
            print('{} loses!'.format(color))
            self.quit()
        color_val = COLOR[color]
        y = Y_AXIS[vertex[0].upper()]
        x = X_AXIS[vertex[1:]]
        p = Point(x, y)
        if not is_legal(self.go, p, color_val):
            print('Move illegal, play the stone at the other places: ')
            return 1
        else:
            self.go.set_color(color_val, p)
            self.move_stack.append(move)
            for neighbor in get_neighbors(p):
                if self.go.get_color(neighbor) == color_val * -1:
                    enemy = get_chain(self.go, neighbor)
                    if len(enemy.liberties) == 0:
                        for point in enemy.stones:
                            self.go.set_color(COLOR['empty'], point)
                            print('updated')
                        self.go.update_captured(color_val * -1, len(enemy.stones))
                        if len(enemy.stones) == 1:
                            self.go.ko_point = enemy.stones.pop()
                        else:
                            self.go.ko_point = None
                else:
                    self.go.ko_point = None
        return 0

    def genmove(self, color):
        """
        Notice that “pass” is a valid vertex and should be returned
        if the engine wants to pass. Use “resign” if you want to
        give up the game. The controller is allowed to use this
        command for either color, regardless who played the last
        move.
        :param color:color color - Color for which to generate a move.
        :return:vertex|string vertex - Vertex where the move was
        played or the string “resign”.
        """
        # TODO
        return

    def undo(self):
        """
        If you want to take back multiple moves, use this command
        multiple times. The engine may fail to undo if the
        move history is empty or if the engine only maintains a
        partial move history, which has been exhausted by previous
        undos. It is never possible to undo handicap placements.
        Use clear board if you want to start over. An
        engine which never is able to undo should not include this
        command among its known commands.
        :return:None
        """
        last_move = self.move_stack.pop()
        vertex = last_move.split()[1]
        # print(vertex)
        y = Y_AXIS[vertex[0].upper()]
        x = X_AXIS[vertex[1:]]
        self.go.set_color(0, Point(x, y))
        return
    # ###################################### End of Core Play Commands #################################################

    # ###################################### Tournament Commands #######################################################
    def time_settings(self, main_time: int, byo_yomi_time: int, byo_yomi_stones: int):
        """
        The interpretation of the parameters is discussed in section
        4.2. The engine must accept the requested values.
        This command gives no provision for negotiation of the
        time settings.
        :param main_time:int main time - Main time measured in seconds.
        :param byo_yomi_time:int byo yomi time - Byo yomi time measured in seconds.
        :param byo_yomi_stones:int byo yomi stones - Number of stones per byo yomi period.
        :return:None
        """
        return

    def time_left(self, color, time, stones):
        """
        While the main time is counting, the number of remaining
        stones is given as 0.
        :param color:color color - Color for which the information applies.
        :param time:int time - Number of seconds remaining.
        :param stones:int stones - Number of stones remaining.
        :return:None
        """
        return

    def final_score(self):
        """
        ask for the engine’s opinion about the score
        :return:string score - Score as described in section 4.3.
        """
        score_black: int = 0
        score_white: int = 0
        chains_black: List[Chain] = []
        chains_white: List[Chain] = []
        for i, row in enumerate(self.go.board):
            for j, col in enumerate(row):
                if self.go.board[i][j] == COLOR['black']:
                    temp_black: Chain = get_chain(self.go, Point(i, j))
                    if temp_black not in chains_black:
                        chains_black.append(temp_black)
                if self.go.board[i][j] == COLOR['white']:
                    temp_white: Chain = get_chain(self.go, Point(i, j))
                    if temp_white not in chains_white:
                        chains_white.append(temp_white)
        for chain_black in chains_black:
            score_black += len(chain_black.stones)
            chainb_empty: Set[Point] = set()
            for p_empty in chain_black.liberties:
                chainb_empty.union(get_chain_points(self.go, p_empty))
            score_black += len(chainb_empty)
            print('black: {}'.format(score_black))
        for chain_white in chains_white:
            score_white += len(chain_white.stones)
            chainw_empty: Set[Point] = set()
            for p_empty in chain_white.liberties:
                chainw_empty.union(get_chain_points(self.go, p_empty))
            score_black += len(chainw_empty)
            print('white: {}'.format(score_white))
        score_difference: float = float(score_black - score_white) - self.komi
        if score_difference > 0:
            return 'B+{}'.format(score_difference)
        elif score_black < score_white + self.komi:
            return 'W+{}'.format(-score_difference)
        else:
            return '0'

    def final_status_list(self, status):
        """
        query an engine about the status of the stones
        :param status:string status - Requested status.
        :return:vertex*& stones - Stones with the requested status.

        """
        return
    # ###################################### End of Tournament Commands ################################################

    # ###################################### Regression Commands #######################################################
    def loadsgf(self, filename, move_number):
        """
        Due to the syntactical limitations of this protocol, the
        filename cannot include spaces, hash signs (#), or control
        characters. The command requires the controller and the
        engine to share file system, or at least that the controller
        has sufficient knowledge about the file system of the engine.
        If move number is larger than the number of moves
        in the file, read until the end of the file. This command has
        no support for sgf files with variations or game collections.
        :param filename:string filename - Name of an sgf file.
        :param move_number:int move number - Optional move number.
        :return:None
        """
        # TODO currently not useful
        return

    def reg_genmove(self, color):
        """
        This command differs from genmove in that it does not
        play the generated move. It is also advisable to turn off
        any move randomization since that may cause meaningless
        regression fluctuations.
        :param color:color color - Color for which to generate a move.
        :return:vertex|string vertex - Vertex where the engine would
        want to play a move or the string “resign”.
        """
        return
    # ###################################### End of Regression Commands ################################################

    # ###################################### Debug Commands ############################################################
    def showboard(self):
        """
        The engine may draw the board as it likes. It is, however,
        required to place the coordinates as described in section
        2.11. This command is only intended to help humans with
        debugging and the output should never need to be parsed
        by another program.
        :return:string*& board - A diagram of the board position.
        """
        print('\n\n')
        str_board = np.array([[STONE_SYMBOL[val] for val in row] for row in self.go.board])
        print('  '.join(['\tA', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']))
        for index, line in enumerate(str_board):
            if index < 9:
                new_line = np.concatenate(([str(index + 1)+' '], line, [str(index + 1)]))
            else:
                new_line = np.concatenate(([str(index + 1)], line, [str(index + 1)]))
            print('  '.join(new_line))

        print('  '.join(['\tA', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']))
        return
