from constants import *
from error import *
from go import *


def opposite_color(color: Color) -> Color:
    if color == 'black':
        return Color('white')
    if color == 'white':
        return Color('black')
    else:
        return color


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


def get_liberties(p: Point, color: Color) -> Set[Point]:
    liberties: Set[Point] = set()
    flood_fill_color: Color = opposite_color(color)
    return liberties

