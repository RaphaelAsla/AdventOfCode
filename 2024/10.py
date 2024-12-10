""" Advent Of Code 2024 : 10 """

from aoctools import *

def trail_dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    trailheads = []
    
    for dir in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
        nbr = (start[0] + dir[0], start[1] + dir[1])
        if nbr in graph and nbr not in visited:
            if graph[nbr] - graph[start] == 1:
                if graph[nbr] == 9:
                    trailheads.append(nbr)
                else:
                    trailheads.extend(trail_dfs(graph, nbr))

    return trailheads

def main(aocd: AOCD):
    map = aocd.igrid

    a = 0
    b = 0

    for pos, height in map.items():
        if height == 0:
            trailheads = trail_dfs(map, pos)
            a += len(set(trailheads))
            b += len(trailheads)

    aocd.p1(a)
    aocd.p2(b)

if __name__ == '__main__':
    aocd = AOCD(2024, 10)
    main(aocd)
