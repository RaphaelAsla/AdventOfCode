""" Advent Of Code 2025 : 9 """

from aoctools import *


def main(aocd: AOCD):
    #aocd.get_example()

    inp = aocd.irows_split_at(',')

    a = 0
    #b = 0

    for i in inp:
        for j in inp:
            if i != j:
                x_diff = abs(i[0] - j[0]) + 1
                y_diff = abs(i[1] - j[1]) + 1
                t = x_diff if x_diff > 0 else 1
                t *= y_diff if y_diff > 0 else 1
                a = max(a, t)

    aocd.p1(a)
    #aocd.p2(b)


if __name__ == '__main__':
    import time
    start = time.time()
    aocd = AOCD(2025, 9)
    main(aocd)
    print(f'Time Taken: {time.time() - start} seconds')
