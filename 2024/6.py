""" Advent Of Code 2024 : 6 """

from aoctools import *

def move(start, grid, p2=False):
    moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    visited = set([start if not p2 else None])
    pos, dir = start, 0
    while True:
        dx, dy = moves[dir]
        next_pos = (pos[0] + dx, pos[1] + dy)
        while next_pos in grid and grid[next_pos] != '#':
            pos = next_pos
            next_pos = (pos[0] + dx, pos[1] + dy)
            if not p2: visited.add(pos)
        if next_pos not in grid:
            return visited, False
        if p2:
            if (pos, dir) in visited:
                return visited, True
            visited.add((pos, dir))
        dir = (dir + 1) % 4

def main(aocd: AOCD):
    a = 0
    b = 0

    grid = aocd.sgrid
    start = next((k for k, v in aocd.sgrid.items() if v == '^'))

    path = move(start, grid)[0]
    a = len(path)

    for pos in path:
        if pos == start:
            continue
        grid[pos] = '#'
        b += move(start, grid, p2=True)[1]
        grid[pos] = '.'

    aocd.p1(a)
    aocd.p2(b)

if __name__ == '__main__':
    aocd = AOCD(2024, 6)
    main(aocd)
