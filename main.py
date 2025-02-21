import time
import curses
import random
import keyboard

mywindow = curses.initscr()

class GameState(object):
    def __init__(self, dim):
        self._matrix = [[random.randint(0,1) for x in range(dim)] for y in range(dim)]
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
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if i >= self.dim:
                    i = 0
                if j >= self.dim:
                    j = 0 
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
                    next[i][j] = 0
                else:
                    next[i][j] = mat[i][j]
        self._matrix = next
                
    def get_matrix_string(self):
        x = ''
        for row in self._matrix:
            x += ' '.join(str(item) for item in row)
            x += "\n"
        return x

if __name__=="__main__":
    game_of_life = GameState(15)
    z = 100
    while z > 1:
        # matrix = update_matrix(matrix)
        # mywindow.addstr(0,0, get_matrix_string(matrix))        
        # mywindow.addstr(0,0, get_matrix_string(matrix))
        mywindow.addstr(0,0, game_of_life.get_matrix_string())
        mywindow.refresh()
        game_of_life.update_matrix()
        z -= 1
        time.sleep(1)

    curses.endwin()
    quit()
