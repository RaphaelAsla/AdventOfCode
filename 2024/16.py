""" Advent Of Code 2024 : 16 """

from aoctools import *
from queue import PriorityQueue

def dijkstra(start, goal, grid):
    pq = PriorityQueue()
    pq.put((1, start, None))
    parent = {}
    visited = {}

    while not pq.empty():
        turns, curr_node, dir = pq.get()

        if curr_node == goal:
            path = []
            while curr_node != start:
                path.append(curr_node)
                curr_node = parent[curr_node]
            return path[::-1], turns

        for new_dir in [Vec(1, 0), Vec(0, -1), Vec(-1, 0), Vec(0, 1)]:
            next_node = curr_node + new_dir
            cost = 1 if dir is not None and dir != new_dir else 0
            new_cost = turns + cost

            if next_node in grid and grid[next_node] != '#':
                if next_node not in visited or visited[next_node] > new_cost:
                    visited[next_node] = new_cost
                    pq.put((new_cost, next_node, new_dir))
                    parent[next_node] = curr_node

    return [], -1


def main(aocd: AOCD):
    a = 0

    grid = aocd.vsgrid

    start = next(k for k, v in grid.items() if v == 'S') 
    goal = next(k for k, v in grid.items() if v == 'E') 
    
    path, cost = dijkstra(start, goal, grid)

    a = len(path) + cost * 1000
    aocd.p1(a)

if __name__ == '__main__':
    aocd = AOCD(2024, 16)
    main(aocd)
