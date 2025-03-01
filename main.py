import time
import curses
import random
import keyboard

class GameState(object):
    def __init__(self, dim):
        self._matrix = [[random.randint(0, 1) for x in range(dim)] for y in range(dim)]
        self.dim = dim

    @property
    def matrix(self):
        return self._matrix

    def swap_matrix(self):
        self._matrix = self.next

    def check_active_neighbors(self, row: int, col: int) -> list:
        # Check the neighbors to a cell. Maximum it can be 8.
        neighbors = 0
        mat = self._matrix
        if row == 0:
            min_row = 0
        else:
            min_row = row - 1

        if row == self.dim - 1:
            max_row = self.dim - 1
        else:
            max_row = row + 1

        if col == 0:
            min_col = 0
        else:
            min_col = col - 1

        if col == self.dim - 1:
            max_col = self.dim - 1
        else:
            max_col = col + 1
        
        for i in range(min_row, max_row + 1):
            for j in range(min_col, max_col + 1):
                if mat[i][j]:
                    neighbors += mat[i][j]
        return neighbors - mat[row][col]

    def update_matrix(self):
        next = [[0 for x in range(self.dim)] for y in range(self.dim)]
        mat = self._matrix
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                neighbors = self.check_active_neighbors(i, j)
                if neighbors < 2 or neighbors > 3:
                    next[i][j] = 0
                elif neighbors == 3:
                    next[i][j] = 1
                else:
                    next[i][j] = mat[i][j]
        self._matrix = next
                
    def get_matrix_string(self):
        x = ''
        for row in self._matrix:
            for item in row:
                if item:
                    x  += '■' + ' '
                else:
                    x += ' ' + ' '
            x += "\n"
        return x

if __name__=="__main__":
    mywindow = curses.initscr()
    height,width = mywindow.getmaxyx()
    num = min(height,width)
    game_of_life = GameState(num - 1)

    while  True:
        mywindow.refresh()
        mywindow.addstr(0,0, game_of_life.get_matrix_string())
        game_of_life.update_matrix()
        time.sleep(0.1)
        mywindow.refresh()
