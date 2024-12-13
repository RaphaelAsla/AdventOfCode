""" Advent Of Code 2024 : 12 """

from aoctools import *
from collections import defaultdict


def dfs(grid, start, visited=None):
    if visited == None:
        visited = set()
    visited.add(start)
    for nbr in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
        nbr = start[0] + nbr[0], start[1] + nbr[1]
        if nbr in grid and nbr not in visited and grid[nbr] == grid[start]:
            dfs(grid, nbr, visited)
    return visited


def find_edges(region):
    F = defaultdict(list)
    total_edges = len(region) * 4
    for plant in region:
        for dir in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            nbr = plant[0] + dir[0], plant[1] + dir[1]
            if nbr in region:
                total_edges -= 1
            else:
                F[plant].append((dir[0], dir[1]))
    return total_edges, F


def find_sides(region, start, facing, visited=None):
    if visited == None:
        visited = set()
    if facing not in region[start]:
        return visited
    visited.add(start)
    for nbr in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
        nbr = start[0] + nbr[0], start[1] + nbr[1]
        if nbr in region and nbr not in visited and facing in region[nbr]:
            find_sides(region, nbr, facing, visited)
    return visited


def main(aocd: AOCD):
    grid = aocd.sgrid

    a = 0
    b = 0

    map_visited = set()
    for plant in grid:
        if plant not in map_visited:
            region = dfs(grid, plant)
            map_visited.update(region)
            sides = defaultdict(int)
            edges, peri_plant_faces = find_edges(region)
            region_visited = set()
            for pplant in peri_plant_faces:
                for dir in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                    if (pplant, dir) not in region_visited:
                        sub_region = find_sides(peri_plant_faces, pplant, dir)
                        if len(sub_region) > 0:
                            sides[dir] += 1
                            region_visited.update((pk, dir) for pk in sub_region)
            area = len(region)
            a += area * edges
            b += area * sum(sides.values())

    aocd.p1(a)
    aocd.p2(b)


if __name__ == "__main__":
    aocd = AOCD(2024, 12)
    main(aocd)
