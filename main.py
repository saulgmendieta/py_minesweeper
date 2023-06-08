from random import randint


class Board:

    def __init__(self, size):
        self.size = size

        self.cells = {}
        for i in range(0, size):
            cell_type = 'nor'
            for j in range(0, size):
                if i == 0 or i == size-1:
                    if j == 0 or j == size - 1:
                        cell_type = 'cor'
                    else:
                        cell_type = 'edg'
                pos = chr(65+i) + str(j + 1)
                self.cells[pos] = Cell(pos, cell_type)

    def print_board(self):

        board_gui = '  '
        for i in range(0, self.size + 1):
            for j in range(0, self.size + 1):
                if i == 0 and j != 0:
                    board_gui += f'  {j}  '
                if j == 0 and i != 0:
                    board_gui += f'{chr(64+i)} '
                if i > 0 and j > 0:
                    pos = chr(64+i) + str(j)
                    board_gui += self.cells[pos].status

            board_gui += f'\r\n'

        return board_gui


class Cell:

    def __init__(self, pos, cell_type):
        self.pos = pos
        self.cell_type = cell_type
        self.status = ' [ ] '


class Game:

    def __init__(self, board, mines):
        self.board = board
        self.mines = mines
        self.mines_list = []

    def place_mines(self):

        for i in range(self.mines):
            not_valid_poss = True
            while not_valid_poss:
                size = self.board.size

                x = randint(0, size - 1)
                y = randint(0, size - 1)

                pos = chr(65+x) + str(y+1)
                if self.board.cells[pos].cell_type != 'cor':
                    if self.board.cells[pos] not in self.mines_list:
                        not_valid_poss = False
                        self.mines_list.append(self.board.cells[pos])


print('Minesweeper')

sz = 5
game_board = Board(5)
game = Game(game_board, mines=3)

game.place_mines()
print(game_board.print_board())
