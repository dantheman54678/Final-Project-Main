import math as m
import random as r

class SudokuGenerator:
    #initialization
    def __init__(self, removed_cells, row_length = 9):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = int(m.sqrt(row_length))
        self.board = []

        #makes empty board
        for i in range(row_length):
            self.board.append([0 for i in range(row_length)])

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(row)

    def valid_in_row(self, row, num):
        for value in self.board[int(row)]:
            if num == value:
                return False
        return True

    def valid_in_col(self, col, num):
        for i in range(self.row_length):
            if num == self.board[i][int(col)]:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for i in range(self.box_length):
            for j in range(self.box_length):
                if num == self.board[row_start + i][col_start + j]:
                    return False
        return True

    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box((row//self.box_length)*self.box_length, (col//self.box_length)*self.box_length, num):
            return True
        else:
            return False

    def fill_box(self, row_start, col_start):
        #goes through box row by row and gives it a unused value
        usable_values = {1,2,3,4,5,6,7,8,9}
        for i in range(self.box_length):
            for j in range(self.box_length):
                if self.board[row_start + i][col_start + j] == 0:
                    self.board[row_start + i][col_start + j] = r.choice(list(usable_values))
                usable_values.remove(self.board[row_start + i][col_start + j])

    def fill_diagonal(self):
        #need to fill boxes along \ diagonal
        self.board[0][0] = r.randint(1, 9)
        self.fill_box(0,0)
        self.board[3][3] = r.randint(1, 9)
        self.fill_box(3,3)
        self.board[6][6] = r.randint(1, 9)
        self.fill_box(6,6)


    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[int(row)][int(col)] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        #randomly picks a cell and removes its value.
        #if cell previously chosen, it skips it
        currently_removed = 0
        while currently_removed < self.removed_cells:
            rand_row, rand_col = r.randint(0, self.row_length - 1), r.randint(0, self.row_length - 1)
            cell = self.board[rand_row][rand_col]
            if cell == 0:
                continue
            else:
                self.board[rand_row][rand_col] = 0
                currently_removed += 1


def generate_sudoku(removed, size):
    sudoku = SudokuGenerator(removed, size)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return completed_board, board
