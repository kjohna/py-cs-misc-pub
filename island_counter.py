import random
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import queue
import time
# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]

# island_counter(islands) # returns 4

# assuming each sub arr is same length


def add_neighbors(x, y, visited):
    # helper function, explores up, right, down, left of a
    # coordinate (x, y) and adds any un-visited 1's to visited
    # basically dfs since recursion effectively a stack
    # up
    if y - 1 > -1:
        if(islands[x][y - 1]):
            one = f"{x},{y - 1}"
            if not one in visited:
                visited.add(one)
                visited = add_neighbors(x, y - 1, visited)
    # right
    if x + 1 < len(islands[0]):
        if(islands[x + 1][y]):
            one = f"{x + 1},{y}"
            if not one in visited:
                visited.add(one)
                visited = add_neighbors(x + 1, y, visited)
    # down
    if y + 1 < len(islands):
        if(islands[x][y + 1]):
            one = f"{x},{y + 1}"
            if not one in visited:
                visited.add(one)
                visited = add_neighbors(x, y + 1, visited)
    # left
    if x - 1 > -1:
        if(islands[x - 1][y]):
            one = f"{x - 1},{y}"
            if not one in visited:
                visited.add(one)
                visited = add_neighbors(x - 1, y, visited)

    return visited


def add_neighbors_bfs(x, y, visited):
    # helper function, explores up, right, down, left of a
    # coordinate (x, y) and adds any un-visited 1's to visited
    # do bfs
    q = queue.Queue()
    q.put((x, y))
    while not q.empty():
        chk = q.get()
        x = chk[0]
        y = chk[1]
        # up
        if y - 1 > -1:
            if(islands[x][y - 1]):
                one = f"{x},{y - 1}"
                if not one in visited:
                    visited.add(one)
                    q.put((x, y - 1))
        # right
        if x + 1 < len(islands[0]):
            if(islands[x + 1][y]):
                one = f"{x + 1},{y}"
                if not one in visited:
                    visited.add(one)
                    q.put((x + 1, y))
        # down
        if y + 1 < len(islands):
            if(islands[x][y + 1]):
                one = f"{x},{y + 1}"
                if not one in visited:
                    visited.add(one)
                    q.put((x, y + 1))
        # left
        if x - 1 > -1:
            if(islands[x - 1][y]):
                one = f"{x - 1},{y}"
                if not one in visited:
                    visited.add(one)
                    q.put((x - 1, y))
    return visited


def island_counter(islands):

    island_count = 0
    visited_bfs = set()
    visited_dfs = set()
    bfs_time = 0
    dfs_time = 0
    for y in range(len(islands)):
        for x in range(len(islands[0])):
            # if there's a 1
            if islands[x][y]:
                # and not already visited
                one = f"{x},{y}"
                if not one in visited_bfs:
                    # increment island count - only do here, not dfs too
                    island_count += 1
                    # add to visited
                    visited_bfs.add(one)
                    # add neighbors - bfs
                    t1 = time.time()
                    visited_bfs = add_neighbors_bfs(x, y, visited_bfs)
                    t2 = time.time()
                    bfs_time += t2 - t1
                if not one in visited_dfs:
                    # add to visited
                    visited_dfs.add(one)
                    # add neighbors - dfs
                    t1 = time.time()
                    visited_dfs = add_neighbors(x, y, visited_dfs)
                    t2 = time.time()
                    dfs_time += t2 - t1
    print(f"bfs: {round(bfs_time, 2)}")
    print(f"dfs: {round(dfs_time, 2)}")

    return island_count


def gen_islands(x_max, y_max):
    islands = []
    for x in range(x_max):
        row = []
        for y in range(y_max):
            row.append(random.choice((0, 1)))
        islands.append(row)
    return islands


# https://github.com/LambdaSchool/Graphs--solution/blob/master/projects/islands/island_generator.py
def generate_island_matrix(width, height, density):
    matrix = []
    for h in range(height):
        matrix.append([0] * width)
    for x in range(width):
        for y in range(height):
            # print(random.random() < density)
            if random.random() < density:
                matrix[y][x] = 1
    return matrix


generate_island_matrix(10, 10, 0.5)


def print_islands(islands):
    # https://stackoverflow.com/questions/43971138/python-plotting-colored-grid-based-on-values
    # create discrete colormap
    cmap = colors.ListedColormap(['blue', 'green'])
    bounds = [0, 1, 1]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    ax.imshow(islands, cmap=cmap, norm=norm)

    # draw gridlines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    # ax.set_xticks(np.arange(-.5, 10, 1))
    # ax.set_yticks(np.arange(-.5, 10, 1))

    plt.show()


if __name__ == '__main__':
    islands = [[0, 1, 0, 1, 0],
               [1, 1, 0, 1, 1],
               [0, 0, 1, 0, 0],
               [1, 0, 1, 0, 0],
               [1, 1, 0, 0, 0]]
    for row in islands:
        print(row)
    print(island_counter(islands))
    # islands = gen_islands(1000, 1000)
    # density > 0.6 seems to break dfs..max recursion depth
    islands = generate_island_matrix(100, 100, .5)
    # for row in islands:
    #     print(row)
    print(island_counter(islands))
    print_islands(islands)
