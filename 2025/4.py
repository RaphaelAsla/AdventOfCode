"""Advent Of Code 2025 : 4"""

from aoctools import *


def main(aocd: AOCD):
    inp = aocd.sgrid

    a = 0
    b = 0

    DIRS_8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    first_iter = True

    while True:
        to_remove = []

        for pos, v in inp.items():
            if v != "@":
                continue

            adj = sum(inp.get((pos[0] + dx, pos[1] + dy), ".") == "@" for dx, dy in DIRS_8)

            if adj < 4:
                if first_iter:
                    a += 1
                to_remove.append(pos)

        if not to_remove:
            break

        for pos in to_remove:
            inp[pos] = "."
            b += 1

        first_iter = False

    aocd.p1(a)
    aocd.p2(b)


if __name__ == "__main__":
    import time

    start = time.time()
    aocd = AOCD(2025, 4)
    main(aocd)
    print(f"Time Taken: {time.time() - start} seconds")
