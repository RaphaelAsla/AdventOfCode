""" Advent Of Code 2024 : 18 """

from aoctools import *
from collections import deque

def find_path(start, goal, grid):
    queue = deque([(start, 0)])
    visted = set([start])

    while queue:
        curr_node, steps = queue.popleft()

        if curr_node == goal:
            return steps

        for dir in [Vec(1, 0), Vec(0, -1), Vec(-1, 0), Vec(0, 1)]:
            next_node = curr_node + dir
            if next_node in grid and next_node not in visted:
                queue.append((next_node, steps + 1))
                visted.add(next_node)

    return 0

def main(aocd: AOCD):
    a = 0
    b = 0

    bts1 = [Vec(*map(int, pair.split(','))) for pair in  aocd.scolumns_split_at('\n')[0][:1024]]
    bts2 = [Vec(*map(int, pair.split(','))) for pair in  aocd.scolumns_split_at('\n')[0][1024:]]
    grid = set(Vec(x, y) for y in range(71) for x in range(71) if Vec(x, y) not in bts1)

    a = find_path(Vec(0, 0), Vec(70, 70), grid)

    for byte in bts2:
        grid.remove(byte) # we remove the node at the position of the fallen byte
        if find_path(Vec(0, 0), Vec(70, 70), grid) == 0:
            b = str(byte[0]) + ',' + str(byte[1])
            break

    aocd.p1(a)
    aocd.p2(b)

if __name__ == '__main__':
    aocd = AOCD(2024, 18)
    main(aocd)
