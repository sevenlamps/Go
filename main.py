import go
from go import *
from controller import Player
from engine import Engine


if __name__ == '__main__':
    move_stack = []
    new_engine = Engine(move_stack, 7.5, 0)
    new_engine.showboard()

    player_b = Player(Color('black'))
    player_w = Player(Color('white'))

    while True:

        while player_b.move(new_engine, Vertex(input())) == 1:
            pass
        new_engine.showboard()
        while player_w.move(new_engine, Vertex(input())) == 1:
            pass
        new_engine.showboard()
