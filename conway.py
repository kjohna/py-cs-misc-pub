from os import system, name
from time import sleep


def conway(board):
    # count_live_neighbors assumes rectangular board
    next_board = [r[:] for r in board]
    count = 0
    while count < 200:
        sleep(.3)
        count += 1
        display_board(board)
        # for each cell
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                # print(f"cell value: {cell} r,c:{r},{c}")
                # get live neighbor count
                live_neighbors = count_live_neighbors(board, r, c)
                # determine if cell lives or dies, populate next_board with update
                # https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
                if cell == 1:
                    # Any live cell with fewer than two live neighbours dies
                    # Any live cell with two or three live neighbours lives on to the next generation.
                    # Any live cell with more than three live neighbours dies
                    if (live_neighbors < 2) or (live_neighbors > 3):
                        next_board[r][c] = 0
                else:
                    # Any dead cell with three live neighbours becomes a live cell
                    if live_neighbors == 3:
                        next_board[r][c] = 1
                # print(f"next_board: {next_board[r][c]}")
        # after next_board is determined, ok to overwrite board
        board = [r[:] for r in next_board]


def count_live_neighbors(board, r, c):
    # count_live_neighbors assumes rectangular board
    nr = len(board)
    nc = len(board[0])
    live_neighbors = 0
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            r_n = r + dr
            c_n = c + dc
            neighbor = 0
            # only check neighbor for valid indices
            # NOTE: no wrap-around, off-board 'neighbors' are dead
            row_neighbor_exists = not(r_n < 0 or r_n >= nr)
            col_neighbor_exists = not(c_n < 0 or c_n >= nc)
            not_self = not(r_n == r and c_n == c)
            if row_neighbor_exists \
                    and col_neighbor_exists \
                    and not_self:
                neighbor = board[r_n][c_n]
            # print(f"neighbor value:{neighbor} r,c:{r_n},{c_n}")
            if neighbor == 1:
                live_neighbors += 1
        # print(
            # f"r,c: {r},{c} = {cell} live neighbors: {live_neighbors}")
    return live_neighbors


def display_board(board):
    clear()
    # print("=========")
    for row in board:
        for cell in row:
            if cell:
                print('* ', end='', flush=True)
            else:
                print('□ ', end='', flush=True)
        print("")


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


if __name__ == '__main__':
    # blinker
    # board = [
    #     [0, 0, 0, 0, 0],
    #     [0, 0, 1, 0, 0],
    #     [0, 0, 1, 0, 0],
    #     [0, 0, 1, 0, 0],
    #     [0, 0, 0, 0, 0],
    # ]
    # glider
    board = [
        [1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    conway(board)
