"""Advent Of Code 2025 : 8"""

from aoctools import *

import math
from collections import Counter
from itertools import combinations


def dist(b1, b2):
    b1x, b1y, b1z = b1
    b2x, b2y, b2z = b2
    return math.sqrt((b1x - b2x) ** 2 + (b1y - b2y) ** 2 + (b1z - b2z) ** 2)


def main(aocd: AOCD):
    inp = [tuple(map(int, line.split(","))) for line in aocd.slist_split_at("\n")]

    a = 0
    b = 0

    edges = []
    for i, j in combinations(range(len(inp)), 2):
        d = dist(inp[i], inp[j])
        edges.append((d, i, j))
    edges = sorted(edges)

    P = list(range(len(inp)))

    def find(i):
        if P[i] != i:
            P[i] = find(P[i])
        return P[i]

    def union(i, j):
        ri = find(i)
        rj = find(j)
        if ri != rj:
            P[rj] = ri

    n = 0
    p = []
    for _, i, j in edges:
        if len(set(p)) == 2 and find(i) != find(j):
            b = inp[i][0] * inp[j][0]
            break
        p = [find(i) for i in range(len(inp))]
        union(i, j)
        if (n := n + 1) == 1000:
            a = math.prod(sorted(Counter(p).values(), reverse=True)[:3])

    aocd.p1(a)
    aocd.p2(b)


if __name__ == "__main__":
    import time

    start = time.time()
    aocd = AOCD(2025, 8)
    main(aocd)
    print(f"Time Taken: {time.time() - start} seconds")
