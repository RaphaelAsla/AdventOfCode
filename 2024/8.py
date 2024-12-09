""" Advent Of Code 2024 : 8 """

from aoctools import *
from math import pi, cos, sin

def cast_ray(origin, direction, max_distance, grid):
    ox, oy = origin
    antinodes_p1 = set()
    antinodes_p2 = set()

    for t in range(1, max_distance):
        pos = Vec(round(ox + t * cos(direction)), round(oy + t * sin(direction)))

        if  pos not in grid or pos == origin:
            break

        if grid[Vec(ox, oy)] == grid[pos]:
            diff = origin - pos

            for tt in (1, -2):
                ant_node = origin + tt * diff
                if ant_node in grid:
                    antinodes_p1.add(ant_node)

            for tt in range(-48, 49):
                ant_node = origin + tt * diff
                if ant_node in grid:
                    antinodes_p2.add(ant_node)
                   
    return antinodes_p1, antinodes_p2

def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

def main(aocd: AOCD):
    grid = aocd.vsgrid

    a = set()
    b = set()

    for pos in grid:
        if grid[pos] == '.':
            continue

        for dir in drange(0.0, 2 * pi, pi / (aocd.grid_width * 2 - 2)):
            max_distance = aocd.grid_width
            hit_antinodes = cast_ray(pos, dir, max_distance, grid)
            a.update(hit_antinodes[0])
            b.update(hit_antinodes[1])

    aocd.p1(len(a))
    aocd.p2(len(b))

if __name__ == '__main__':
    aocd = AOCD(2024, 8)
    main(aocd)
