from go import *
from rule import *
from engine import Engine
from controller import Player


move_stack = []
new_engine = Engine(move_stack, 7.5, 0)
new_engine.showboard()

player_b = Player(Color('black'))
player_w = Player(Color('white'))

# stone capture
# player_b.move(new_engine, Vertex('A17'))
# player_w.move(new_engine, Vertex('M19'))
# player_b.move(new_engine, Vertex('B17'))
# player_w.move(new_engine, Vertex('B19'))
# player_b.move(new_engine, Vertex('A19'))
# player_w.move(new_engine, Vertex('A18'))
# player_b.move(new_engine, Vertex('C18'))
# player_w.move(new_engine, Vertex('B18'))
# player_b.move(new_engine, Vertex('C19'))
# player_w.move(new_engine, Vertex('S18'))
# player_b.move(new_engine, Vertex('A19'))

# ko rule
player_b.move(new_engine, Vertex('D16'))
player_w.move(new_engine, Vertex('C16'))
player_b.move(new_engine, Vertex('C15'))
player_w.move(new_engine, Vertex('D17'))
player_b.move(new_engine, Vertex('D14'))
player_w.move(new_engine, Vertex('E16'))
player_b.move(new_engine, Vertex('E15'))
player_w.move(new_engine, Vertex('D15'))
player_b.move(new_engine, Vertex('D16'))
player_b.move(new_engine, Vertex('D1'))
player_w.move(new_engine, Vertex('S18'))
player_b.move(new_engine, Vertex('D16'))
