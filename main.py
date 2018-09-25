import go
from player import Player

if __name__ == '__main__':
    new_board = go.Board()
    new_board.reset()
    new_board.display()

    player_b = Player('black')
    player_w = Player('white')

    while True:
        player_b.move(new_board, input())
        new_board.display()
        player_w.move(new_board, input())
        new_board.display()
