""" Advent Of Code 2024 : 14 """

from aoctools import *
from collections import defaultdict, deque

def cbfs(grid, start):
    queue = deque()
    queue.append(start)

    visited = set()
    visited.add(start)

    while queue:
        node = queue.popleft()
        for nbr in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            nbr = (node[0] + nbr[0], node[1] + nbr[1])
            if nbr in grid and nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)

    return visited

def main(aocd: AOCD):
    a = 1
    b = 0

    data = aocd.slist_split_at('\n')

    pos_vel = []
    for entry in data:
        parts = entry.split()
        pos = list(map(int, parts[0][2:].split(',')))
        vel = list(map(int, parts[1][2:].split(',')))
        pos_vel.append([pos, vel])


    width = 101
    height = 103
    pos_vel_100 = []

    frames = 1
    found = False
    while not found:
        for i in range(len(pos_vel)):
            for _ in range(abs(pos_vel[i][1][0])):
                pos_vel[i][0][0] += (1 if pos_vel[i][1][0] > 0 else -1)
                if pos_vel[i][0][0] >= width:
                    pos_vel[i][0][0] = 0
                elif pos_vel[i][0][0] < 0:
                    pos_vel[i][0][0] = width - 1
            for _ in range(abs(pos_vel[i][1][1])):
                pos_vel[i][0][1] += (1 if pos_vel[i][1][1] > 0 else -1)
                if pos_vel[i][0][1] >= height:
                    pos_vel[i][0][1] = 0
                elif pos_vel[i][0][1] < 0:
                    pos_vel[i][0][1] = height - 1

        pos_only = [(x[0][0], x[0][1]) for x in pos_vel]

        seen = set()
        for pos in pos_only:
            if pos not in seen:
                cluster = cbfs(pos_only, pos)
                seen.update(cluster)
                if len(cluster) > 15: # We basically search if a cluster larger than a threshold of 15 exists in the grid
                    b = frames
                    found = True
                    break

        if frames == 100:
            pos_vel_100 = pos_vel

        frames += 1

    Q = defaultdict(int)
    half_width = width // 2
    half_height = height // 2

    for cx in range(2):
        for cy in range(2):
            start_x = 0 if cx == 0 else half_width + 1
            end_x = half_width if cx == 0 else width
            start_y = 0 if cy == 0 else half_height + 1
            end_y = half_height if cy == 0 else height
            for (x, y), _ in pos_vel_100:
                if start_x <= x < end_x and start_y <= y < end_y:
                    Q[cx, cy] += 1

    for v in Q.values():
        if v > 0:
            a *= v

    aocd.p1(a)
    aocd.p2(b)

if __name__ == '__main__':
    aocd = AOCD(2024, 14)
    main(aocd)
