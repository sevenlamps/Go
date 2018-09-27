from constants import *
from error import *
from go import *


def get_neighbors(p: Point) -> List[Point]:
    neighbors: List[Point] = []
    if p.x > 0:
        neighbors.append(Point(p.x - 1, p.y))
    if p.x < BOARD_LENGTH - 1:
        neighbors.append(Point(p.x + 1, p.y))
    if p.y > 0:
        neighbors.append(Point(p.x, p.y - 1))
    if p.y < BOARD_LENGTH - 1:
        neighbors.append(Point(p.x, p.y + 1))
    return neighbors


def get_liberties(board: Board, p: Point) -> Set[Point]:
    liberties: Set[Point] = set()
    color_val: int = board.get_color(p)
    flood_filled: Set[int] = set()
    queue: Deque[Point] = deque()
    queue.append(p)
    while queue:
        N: Point = queue.pop()
        east: Point = N
        west: Point = N
        while east.y < BOARD_LENGTH - 1:
            east_of_east: Point = Point(east.x, east.y + 1)
            if board.get_color(east_of_east) == color_val:
                east = east_of_east
            else:
                break
        while west.y > 0:
            west_of_west: Point = Point(west.x, west.y - 1)
            if board.get_color(west_of_west) == color_val:
                west = west_of_west
            else:
                break
        if east.y < BOARD_LENGTH - 1:
            if board.get_color(Point(east.x, east.y + 1)) == COLOR['empty']:
                liberties.add(Point(east.x, east.y + 1))
        if west.y > 0:
            if board.get_color(Point(west.x, west.y - 1)) == COLOR['empty']:
                liberties.add(Point(west.x, west.y - 1))
        for var in range(west.y, east.y):
            p = Point(N.x, var)
            if p.x > 0:
                if board.get_color(Point(p.x - 1, p.y)) == color_val and p.x - 1 not in flood_filled:
                    queue.append(Point(p.x - 1, p.y))
            if p.x < BOARD_LENGTH - 1:
                if board.get_color(Point(p.x + 1, p.y)) == color_val and p.x + 1 not in flood_filled:
                    queue.append(Point(p.x + 1, p.y))
        flood_filled.add(N.x)
    return liberties


def in_atari(board: Board, p: Point) -> bool:
    return len(get_liberties(board, p)) == 1


def is_legal(board: Board, p: Point, color_val: int) -> bool:
    # is the point already occupied
    if board.get_color(p) != COLOR['empty']:
        return False
    # is p is a ko point
    if p in board.ko_point:
        return False
    suicide: bool = True
    for neighbor in get_neighbors(p):
        if board.get_color(neighbor) == COLOR['empty']:
            suicide = False
        elif board.get_color(neighbor) == color_val:
            if not in_atari(board, neighbor):
                suicide = False
        elif board.get_color(neighbor) == color_val * -1:
            enemy: Chain = get_chain(board, neighbor)
            if enemy.in_atari():
                suicide = False
                # for point in enemy.stones:
                #     board.set_color(COLOR['empty'], point)
                #     board.update_captured(color_val * -1, len(enemy.stones))
    if suicide:
        return False
    return True


def get_chain_points(board: Board, p: Point) -> Set[Point]:
    stones: Set[Point] = set()
    stones.add(p)
    color_val = board.get_color(p)
    flood_filled: Set[int] = set()
    queue: Deque[Point] = deque()
    queue.append(p)
    while queue:
        N: Point = queue.pop()
        east: Point = N
        west: Point = N
        while east.y < BOARD_LENGTH - 1:
            east_of_east: Point = Point(east.x, east.y + 1)
            if board.get_color(east_of_east) == color_val:
                east = east_of_east
            else:
                break
        while west.y > 0:
            west_of_west: Point = Point(west.x, west.y - 1)
            if board.get_color(west_of_west) == color_val:
                west = west_of_west
            else:
                break
        for var in range(west.y, east.y + 1):
            p: Point = Point(N.x, var)
            stones.add(p)
            if p.x > 0:
                if board.get_color(Point(p.x - 1, p.y)) == color_val and p.x not in flood_filled:
                    queue.append(Point(p.x - 1, p.y))
            if p.x < BOARD_LENGTH - 1:
                if board.get_color(Point(p.x + 1, p.y)) == color_val and p.x not in flood_filled:
                    queue.append(Point(p.x + 1, p.y))
        flood_filled.add(N.x)
    return stones


def get_chain(board: Board, p: Point) -> Chain:
    stones: Set[Point] = get_chain_points(board, p)
    liberties: Set[Point] = set()
    for stone in stones:
        for neighbor in get_neighbors(stone):
            if board.get_color(neighbor) == COLOR['empty']:
                liberties.add(neighbor)
    return Chain(stones, liberties)




