class Board:

    def __init__(self, size):
        self.size = size


class Game:

    def __init__(self, board, mines):
        self.board = board
        self.mines = mines


print('Minesweeper')

game_board = Board(5)
game = Game(game_board, 3)
