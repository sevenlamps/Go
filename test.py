from go import *
from rule import *
from engine import Engine
from controller import Player


move_stack = []
new_engine = Engine(move_stack, DEFAULT_KOMI, 0)
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
# player_b.move(new_engine, Vertex('D16'))
# player_w.move(new_engine, Vertex('C16'))
# player_b.move(new_engine, Vertex('C15'))
# player_w.move(new_engine, Vertex('D17'))
# player_b.move(new_engine, Vertex('D14'))
# player_w.move(new_engine, Vertex('E16'))
# player_b.move(new_engine, Vertex('E15'))
# player_w.move(new_engine, Vertex('D15'))
# player_b.move(new_engine, Vertex('D16'))
# player_b.move(new_engine, Vertex('D1'))
# player_w.move(new_engine, Vertex('S18'))
# player_b.move(new_engine, Vertex('D16'))


# move
# i: int = 0
# for number in [str(x) for x in range(1, 20)]:
#     for char in 'ABCDEFGHJKLMNOPQRST':
#         if i % 2 == 0:
#             player_w.move(new_engine, Vertex(char + number))
#         else:
#             player_b.move(new_engine, Vertex(char + number))
#         i += 1
#
# print(new_engine.final_score())


# new_engine.loadsgf('sgf_files/LiChangHao_VS_CaoXunXuan_191/李昌镐曹薰铉激斗谱/426.sgf')
#
# for cnt, node in enumerate(new_engine.collection.children[0].nodes[1:]):
#     move: Move = Move('{}{}'.format(node.current_property, node.current_prop_value[0]))
#     new_engine.play(Move(move))
#     new_engine.showboard()
#
# new_engine.final_score()
#
# print('hi')




