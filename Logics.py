import random

def startGame():
    mat = [[0] * 4 for _ in range(4)]
    return mat

def add_new_2(mat):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        mat[r][c] = 2 if random.random() < 0.9 else 4

def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):  # Merge cells in a row
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                changed = True
    return mat, changed

def reverse(mat):
    return [row[::-1] for row in mat]

def transpose(mat):
    return [[mat[j][i] for j in range(4)] for i in range(4)]

def compress(mat):
    changed = False
    new_mat = [[0] * 4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_mat, changed

def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'
            if mat[i][j] == 0:  # Empty space exists
                return 'GAME NOT OVER'
    for i in range(4):
        for j in range(3):  # Check horizontal adjacent cells
            if mat[i][j] == mat[i][j + 1]:
                return "GAME NOT OVER"
    for j in range(4):
        for i in range(3):  # Check vertical adjacent cells
            if mat[i][j] == mat[i + 1][j]:
                return "GAME NOT OVER"
    return "LOST"

def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    return compress(new_grid)[0], changed

def move_right(grid):
    reversed_grid = reverse(grid)
    new_grid, changed1 = compress(reversed_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    final_grid = reverse(compress(new_grid)[0])
    return final_grid, changed

def move_up(grid):
    transposed_grid = transpose(grid)
    new_grid, changed1 = compress(transposed_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    final_grid = transpose(compress(new_grid)[0])
    return final_grid, changed

def move_down(grid):
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid, changed1 = compress(reversed_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    final_grid = transpose(reverse(compress(new_grid)[0]))
    return final_grid, changed
