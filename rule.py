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




