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
# stdscr = curses.initscr()

mywindow = curses.initscr()

matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' '],]

def check_neighbors(x: int, y: int) -> list:
    # Check the neighbors to a cell. Maximum it can be 8.
    x_len = len(matrix[:][0]) - 1
    y_len = len([i[0] for i in matrix]) - 1

    min_x = max(x - 1, 0)
    max_x = min(x + 1, x_len)

    min_y = max(y - 1, 0)
    max_y = min(y + 1, y_len)

    neighbors = []
    for row in range(min_y, max_y + 1):
        for col in range(min_x, max_x + 1):
            # TODO: Fix this!!!
            if x != col and y != row:
                neighbors.append([col, row])
    return neighbors
    

def fewer_than_two(x: int, y: int):
    # If a cell has fewer than two alive neighbors it dies
    if len(check_neighbors(x, y)) < 2:
        return -1
    return 0
    
def more_than_three(x: int, y: int):
    # If a cell has more than three alive neighbors it dies
    if len(check_neighbors(x, y)) > 3:
        return -1
    return 0

def revive(x: int, y: int):
    # Any cell with exactly three alive neighbors becomes live
    if len(check_neighbors(x, y)) == 3:
        return 1
    return 0


def updateMatrix(m):
    action = (fewer_than_two() +
             more_than_three() +
             revive())
    
    if action == 1:
        m[x][y] = "■"
    
    elif action == 0:
        pass

    else: 
        m[x][y] = " "

    return m

def getMarixString(m):
    x = ''
    for row in m:
        x += ' '.join(str(item) for item in row)
        x += "\n"
    return x

print(check_neighbors(0, 0))
print(check_neighbors(5, 5))
print(check_neighbors(9, 9))
# z = 100
# while z > 1:
#     matrix = updateMatrix(matrix)
#     mywindow.addstr(0,0, getMarixString(matrix))
#     mywindow.refresh()
#     z -= 1
#     time.sleep(0.5)

# curses.endwin()
# quit()
