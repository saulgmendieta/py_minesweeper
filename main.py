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


class Cell:

    def __init__(self, pos, cell_type):
        self.pos = pos
        self.cell_type = cell_type


class Game:

    def __init__(self, board, mines):
        self.board = board
        self.mines = mines


print('Minesweeper')

sz = 5
game_board = Board(5)
game = Game(game_board, 5)

cells = game_board.cells
for ii in range(0, sz):
    str_p = ''
    for jj in range(0, sz):
        ps = chr(65+ii) + str(jj + 1)
        str_p += cells[ps].pos + ' '
    print(str_p)
