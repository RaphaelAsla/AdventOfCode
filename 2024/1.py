""" Advent Of Code 2024 : 1 """

from aoctools import *


def main(aocd: AOCD):
    l, r = aocd.icolumns
    aocd.p1(sum(abs(int(x) - int(y)) for x, y in zip(sorted(l), sorted(r))))
    aocd.p2(sum(int(c) * r.count(c) for c in l))

if __name__ == '__main__':
    aocd = AOCD(2024, 1)
    main(aocd)
