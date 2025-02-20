# import dearpygui.dearpygui as dpg

# SIZE = 500
# CELLS = int(SIZE / 10)
# button_params = {
#     "width": 8,
#     "height": 8,
# }
# a = 0
# def save_callback(tag: int):
#     print(tag)

# dpg.create_context()
# dpg.create_viewport()
# dpg.setup_dearpygui()
# with dpg.window(label="Game of Life", width=SIZE, height=SIZE):
#     for y in range(CELLS):
#         for x in range(CELLS):
#             tag= y * 10 + x
#             dpg.add_button(**button_params, pos=[x*10, y*10], callback=save_callback(tag), tag = tag)

# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()


import time
import curses
import random
import keyboard

mywindow = curses.initscr()
        #   0    1    2    3    4    5    6    7    8    9
matrix = [['■', ' ', ' ', ' '], # 0
          ['■', ' ', ' ', ' '], # 1
          ['■', ' ', ' ', ' '], # 2
          [' ', ' ', ' ', ' '], # 3
          [' ', ' ', ' ', ' ']] # 4


class GameState(object):
    def __init__(self, matrix):
        self._matrix = matrix

    @property
    def matrix(self):
        return self._matrix

    def set_board_cell(self, x: int, y: int):
        matrix = self._matrix
        matrix[x][y] = '■'
        self._matrix = matrix

    def reset_board_cell(self, x: int, y: int):
        matrix = self._matrix
        matrix[x][y] = ' '
        self._matrix = matrix

    def check_active_neighbors(self, x: int, y: int) -> list:
        # Check the neighbors to a cell. Maximum it can be 8.
        x_len = len(self.matrix[:][0]) - 1
        y_len = len([i[0] for i in self.matrix]) - 1

        min_x = max(x - 1, 0)
        max_x = min(x + 1, x_len)

        min_y = max(y - 1, 0)
        max_y = min(y + 1, y_len)

        neighbors = []

        for i in range(min_x, max_x + 1):
            for j in range(min_y, max_y + 1):
                if self.matrix[j][i] != ' ':
                    neighbors.append([i, j])
        try:
            neighbors.remove([y, x])
        except:
            pass
        return neighbors
        

    def fewer_than_two(self, x: int, y: int):
        # If a cell has fewer than two alive neighbors it dies
        if len(self.check_active_neighbors(x, y)) < 2:
            print("Fewer")
            return True
        return False
        
    def more_than_three(self, x: int, y: int):
        # If a cell has more than three alive neighbors it dies
        if len(self.check_active_neighbors(x, y)) > 3:
            print("More")
            return True
        return False

    def stable_cell(self, x: int, y: int):
        # If a cell has more than three alive neighbors it dies
        if len(self.check_active_neighbors(x, y)) == 2:
            print("Stable")
            return True
        return False 

    def revive(self, x: int, y: int):
        # Any cell with exactly three alive neighbors becomes live
        if len(self.check_active_neighbors(x, y)) == 3:
            print("Revive")
            return True
        return False

    def update_matrix(self):
        print("This works")
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print("We are inside the loop!")
                if self.fewer_than_two(i, j):                    
                    self.reset_board_cell(i, j)
                elif self.stable_cell(i, j):
                    pass
                elif self.revive(i, j):
                    self.set_board_cell(i, j)
                elif self.more_than_three(i, j):
                    self.reset_board_cell(i, j)
                else:
                    print("There is something wrong!")
                    raise Exception
        return self.matrix
                
    def get_matrix_string(self):
        x = ''
        for row in self.matrix:
            x += ' '.join(str(item) for item in row)
            x += "\n"
        return x

# active = check_active_neighbors(4, 6, matrix)
# print(revive(4, 6, matrix))
# print(fewer_than_two(4, 6, matrix))
# print(more_than_three(4, 6, matrix))
# print("-----")
# active = check_active_neighbors(2, 3, matrix)
# print(fewer_than_two(2, 2, matrix))
# print("-----")
# active = check_active_neighbors(5, 6, matrix)
# print(active)
# print("-----")
# print(fewer_than_two(0,0, matrix))

if __name__=="__main__":
    game_of_life = GameState(matrix=matrix)
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
