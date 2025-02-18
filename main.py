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
matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' '], # 0
          [' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' '], # 1
          [' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' '], # 2
          [' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' '], # 3
          [' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' '], # 4
          [' ', ' ', ' ', ' ', ' ', '■', ' ' ,' ', ' ', ' '], # 5
          [' ', ' ', ' ', ' ', ' ', '■', ' ' ,' ', ' ', ' '], # 6
          [' ', ' ', ' ', ' ', ' ', '■', ' ' ,' ', ' ', ' '], # 7
          [' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' '], # 8
          [' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' '],]# 9

def check_active_neighbors(x: int, y: int, m) -> list:
    # Check the neighbors to a cell. Maximum it can be 8.
    x_len = len(m[:][0]) - 1
    y_len = len([i[0] for i in m]) - 1

    min_x = max(x - 1, 0)
    max_x = min(x + 1, x_len)

    min_y = max(y - 1, 0)
    max_y = min(y + 1, y_len)

    neighbors = []

    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if m[j][i] != ' ':
                neighbors.append([i, j])
    try:
        neighbors.remove([y, x])
    except:
        pass
    print(neighbors)
    return neighbors
    

def fewer_than_two(x: int, y: int, m):
    # If a cell has fewer than two alive neighbors it dies
    if len(check_active_neighbors(x, y, m)) < 2:
        return -1
    return 0
    
def more_than_three(x: int, y: int, m):
    # If a cell has more than three alive neighbors it dies
    if len(check_active_neighbors(x, y, m)) > 3:
        return -1
    return 0

def revive(x: int, y: int, m):
    # Any cell with exactly three alive neighbors becomes live
    if len(check_active_neighbors(x, y, m)) == 3:
        return 1
    return 0


def update_matrix(m):
    # Check the neighbors to a cell. Maximum it can be 8.
    x_len = len(m[:][0]) - 1
    y_len = len([i[0] for i in m]) - 1

    for x in range(0, x_len + 1):
        for y in range(0, y_len + 1):
            action = (fewer_than_two(x, y, m) +
                    more_than_three(x, y, m) +
                    revive(x, y, m))            
            if action == 1:
                m[x][y] = "■"
            
            elif action == 0:
                pass

            else:
                m[x][y] = " "
    return m

def get_matrix_string(m):
    x = ''
    for row in m:
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


z = 100
while z > 1:
    # matrix = update_matrix(matrix)
    # mywindow.addstr(0,0, get_matrix_string(matrix))        
    # mywindow.addstr(0,0, get_matrix_string(matrix))
    mywindow.addstr(0,0, get_matrix_string(matrix))
    mywindow.refresh()
    matrix = update_matrix(matrix)
    z -= 1
    while True:
        if keyboard.is_pressed('space'):
            time.sleep(1)            
            break

curses.endwin()
quit()
