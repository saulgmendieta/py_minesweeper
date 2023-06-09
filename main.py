from random import randint


class Board:

    def __init__(self, size):
        self.size = size

        self.cells = {}
        self.remains = {}
        for i in range(0, size):
            for j in range(0, size):
                cell_type = 'nor'
                if i == 0 or i == size-1:
                    if j == 0 or j == size - 1:
                        cell_type = 'cor'
                    else:
                        cell_type = 'edg'
                elif j == 0 or j == size-1:
                    cell_type = 'edg'
                pos = chr(65+i) + str(j + 1)
                self.cells[pos] = Cell(pos, cell_type)
                self.remains[pos] = Cell(pos, cell_type)

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
        self.value = '0'


class Game:

    def __init__(self, board, mines):
        self.board = board
        self.mines = mines
        self.mines_list = []
        self.win_status = False

    def place_mines(self):

        board = self.board

        for i in range(self.mines):
            not_valid_poss = True
            while not_valid_poss:
                size = board.size

                x = randint(0, size - 1)
                y = randint(0, size - 1)

                pos = chr(65+x) + str(y+1)
                if board.cells[pos].cell_type != 'cor':
                    if board.cells[pos] not in self.mines_list:
                        not_valid_poss = False
                        board.cells[pos].value = '*'
                        self.mines_list.append(board.cells[pos])
                        # print(pos)

        for cell in board.cells:
            size = board.size
            mine_count = 0
            c_cell_x = ord(cell[0])-65
            c_cell_y = int(cell[1])-1
            if board.cells[cell].value != '*':
                for i in range(0, 3):
                    for j in range(0, 3):
                        x = c_cell_x + i-1
                        y = c_cell_y + j-1
                        if 0 <= x < size and 0 <= y < size:
                            pos = chr(65 + x) + str(y + 1)
                            if board.cells[pos].value == '*':
                                mine_count += 1
                board.cells[cell].value = mine_count

    def verify_cell(self, coord):
        game_status = True
        for mine in self.mines_list:
            # print(mine.pos)
            if mine.pos == coord:
                game_status = False

        if game_status:
            self.board.cells[coord].status = f' [{self.board.cells[coord].value}] '
            rem_keys = list(game_board.remains.keys())
            if coord in rem_keys:
                self.board.remains.pop(coord)

        remaining = len(game_board.remains) - self.mines
        if remaining == 0:
            game_status = False
            self.win_status = True

        return game_status


if __name__ == "__main__":
    print('Minesweeper')

    sz = 5
    game_board = Board(5)
    game = Game(game_board, mines=3)

    game.place_mines()

    game_on = True

    keys = list(game_board.cells.keys())

    while game_on:
        print(game_board.print_board())

        coordinate = input('Put a coordinate (A1 format):')
        if coordinate not in keys:
            print("Not valid coordinate\n")
        else:
            game_on = game.verify_cell(coordinate)

    for c in game_board.cells:
        game_board.cells[c].status = f' [{game_board.cells[c].value}] '

    if game.win_status:
        print(game_board.print_board())
        print("\nYou win!")
    else:
        print(game_board.print_board())
        print("\nGame Over")
