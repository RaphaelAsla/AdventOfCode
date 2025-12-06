""" Advent Of Code 2025 : 1 """

from aoctools import *


def main(aocd: AOCD):
    inp = list(map(lambda x: [x[0], int(x[1:])], aocd.slist))

    a = 0
    b = 0

    pos = 50

    for k, v in inp:
        for _ in range(v):
            if k == 'L':
                pos += 99
            elif k == 'R':
                pos += 1

            pos %= 100

            if pos == 0:
                b += 1

        if pos == 0:
            a += 1

    aocd.p1(a)
    aocd.p2(b)


if __name__ == '__main__':
    import time
    start = time.time()
    aocd = AOCD(2025, 1)
    main(aocd)
    print(f'Time Taken: {time.time() - start} seconds')
