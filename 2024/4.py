""" Advent Of Code 2024 : 4 """

from aoctools import *

def in_grid(x, y):
    return x >= 0 and y >= 0 and x < aocd.grid_width and y < aocd.grid_height

def main(aocd: AOCD):
    a = 0
    b = 0

    dirs = {(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)}
    rot_dirs = [{(-1, 1) : 'M', (1, 1) : 'S', (1, -1) : 'S', (-1, -1): 'M'},
                {(-1, 1) : 'M', (1, 1) : 'M', (1, -1) : 'S', (-1, -1): 'S'},
                {(-1, 1) : 'S', (1, 1) : 'M', (1, -1) : 'M', (-1, -1): 'S'},
                {(-1, 1) : 'S', (1, 1) : 'S', (1, -1) : 'M', (-1, -1): 'M'}]

    grid = aocd.sgrid

    for c in grid:
        if grid[c] == 'X':
            a += sum("MAS" == "".join("".join(grid[c[0] + d[0] * i, c[1] + d[1] * i]) for i in range(1, 4) if in_grid(c[0] + d[0] * i, c[1] + d[1] * i)) for d in dirs)
        elif grid[c] == 'A':
            b += sum(all(in_grid(c[0] + d[0], c[1] + d[1]) and grid[c[0] + d[0], c[1] + d[1]] == dir[d] for d in dir) for dir in rot_dirs)

    aocd.p1(a)
    aocd.p2(b)

if __name__ == '__main__':
    aocd = AOCD(2024, 4)
    main(aocd)
