""" Advent Of Code 2024 : 15 """

from aoctools import *
from collections import deque

def move(robot, map, moves):
    M = {'>' : Vec(1, 0), '^' : Vec(0, -1), '<' : Vec(-1, 0), 'v' : Vec(0, 1)}

    def search_dir(pos, dir):
        linked = deque()
        next = pos + dir

        while next in map and map[next] == 'O':
            linked.append(next)
            next += dir

        return linked

    for move in moves:
        dxy = M[move]
        next_pos = robot + dxy
        infront = search_dir(robot, dxy)

        map[robot] = '.'
        if infront and map[infront[-1] + dxy] != '#':
            while infront:
                box = infront.pop()
                map[box] = '.'
                map[box + dxy] = 'O'
            robot = next_pos
        elif not infront and map[next_pos] != '#':
            robot = next_pos
        map[robot] = '@'

    return map

def main(aocd: AOCD):
    a = 0

    map, moves = aocd.slist_split_at('\n\n')
    moves = moves.replace('\n', '')
    map = map.split('\n')

    map = {Vec(x, y): char for y, row in enumerate(map) for x, char in enumerate(row)}
    robot = next((vec for vec, char in map.items() if char == '@'), None)
    final = move(robot, map, moves)

    boxes = [k for k, v in final.items() if v == 'O']
    a = sum(100 * y + x for (x, y) in boxes)

    aocd.p1(a)

if __name__ == '__main__':
    aocd = AOCD(2024, 15)
    main(aocd)
