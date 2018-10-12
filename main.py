import go
from go import *
from controller import Player
from engine import Engine
from rule import movable_points


if __name__ == '__main__':
    move_stack: List = []
    new_engine: Engine = Engine(move_stack, 7.5, 0)
    new_engine.showboard()

    player_b: Player = Player(Color('black'))
    player_w: Player = Player(Color('white'))

    color = 0
    while movable_points(new_engine.go, color):

        while player_b.move(new_engine, Vertex(input())) == 1:
            pass
        color += 1
        color %= 2
        while player_w.move(new_engine, Vertex(input())) == 1:
            pass
        color += 1
        color %= 2

    new_engine.final_score()

