""" Advent Of Code 2024 : 20 """

from aoctools import *

def find_path(start, goal, grid):
    current = start
    path = {start : 0}
    while current != goal:
        for nbr in [Vec(1, 0), Vec(0, -1), Vec(-1, 0), Vec(0, 1)]:
            next_node = current + nbr
            if next_node in grid and next_node not in path:
                current = next_node
                path[current] = len(path)
                break
    return path

def p1cheat(init_path):
    cheats = 0
    for pos in init_path:
        for nbr in [Vec(1, 0), Vec(0, -1), Vec(-1, 0), Vec(0, 1)]:
            next_node = pos + nbr
            if next_node not in init_path:
                next_node = pos + nbr * 2
                if next_node in init_path and (init_path[next_node] - init_path[pos] - 2) >= 100:
                    cheats += 1
    return cheats

def p2cheat(init_path):
    cheats = 0
    radius = 20
    for pos in init_path:
        for x in range(pos[0] - radius, pos[0] + radius + 1):
            yoff = radius - abs(pos[0] - x)
            for y in range(pos[1] - yoff, pos[1] + yoff + 1):
                jump = Vec(x, y)
                man_dist = abs(x - pos[0]) + abs(y - pos[1])
                if jump in init_path and (init_path[jump] - init_path[pos] - man_dist) >= 100:
                    cheats += 1
    return cheats

def main(aocd: AOCD):
    a = 0
    b = 0

    grid = aocd.vsgrid
    start = next(k for k, v in grid.items() if v == 'S')
    end = next(k for k, v in grid.items() if v == 'E')
    grid = set(k for k, v in grid.items() if v != '#')

    init_path = find_path(start, end, grid)

    a = p1cheat(init_path)
    b = p2cheat(init_path)

    aocd.p1(a)
    aocd.p2(b)

if __name__ == '__main__':
    aocd = AOCD(2024, 20)
    main(aocd)
