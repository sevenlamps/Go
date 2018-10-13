from math import sqrt, log
from utility import *
from rule import *
from go import *
from copy import deepcopy


UCT_CONST: float = 1 / sqrt(2)


class Move(NamedTuple):
    point: Point
    color: int


class Node(object):
    def __init__(self, board=None, parent=None, last_move=None):
        self.board: Board = deepcopy(board)
        self.last_move: Point = last_move.point  # TODO to confirm whether the color variable is necessary
        self.parent: Node = parent
        self.child: List[Node] = []
        self.visits: int = 0
        self.rewards: List[float] = []
        self.cur_player: int = last_move.color
        self.untried_point: List[Point] = movable_points(self.board, self.cur_player)


def backup_negamax(v: Node, terminal_reward: float):  # two-player version
    while v:
        v.visits += 1
        v.rewards.append(terminal_reward)
        terminal_reward = -terminal_reward
        v = v.parent
    return


def default_policy(board: Board, color_val: int) -> float:  # TODO whether param should be state or be board
    board_copy: Board = deepcopy(board)
    while movable_points(board_copy, color_val):
        p: Point = np.random.choice(movable_points(board_copy, color_val))
        make_move(board_copy, color_val, p)
    score_black = get_final_score(board_copy, COLOR['black'])
    score_white = get_final_score(board_copy, COLOR['white'])
    return get_reward(score_black, score_white)


def best_child(v: Node, k=UCT_CONST) -> Node:
    return max(v.child, key=lambda c: c.rewards / c.visits + k * sqrt(2 * log(c.parent.visits / c.visits)))


def expand(v: Node) -> Node:
    p: Point = np.random.choice(v.untried_point)
    v.untried_point.remove(p)
    v_new: Node = Node(v.board, v, Move(p, -v.cur_player))
    make_move(v_new.board, v_new.cur_player, p)
    v_new.last_move = Move(p, v_new.cur_player)
    return v_new


def tree_policy(v: Node) -> Node:
    while movable_points(v.board, v.cur_player):
        if v.untried_point:
            return expand(v)
        else:
            v = best_child(v)
    return v


def uct_search(root_state: Node, itermax: int) -> Point:
    v_root: Node = Node(root_state)
    for i in range(itermax):
        v_last: Node = tree_policy(v_root)
        reward: float = default_policy(v_last.board, v_last.cur_player)
        backup_negamax(v_last, reward)
    return best_child(v_root, 0).last_move
