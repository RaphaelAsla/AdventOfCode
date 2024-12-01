""" Advent Of Code 2024 : 1 """

from aoctools import *


def main(aocd: AOCD):
    l, r = aocd.imultilist
    aocd.p1(sum(abs(x - y) for x, y in zip(sorted(l), sorted(r))))
    aocd.p2(sum(c * r.count(c) for c in l))

if __name__ == '__main__':
    aocd = AOCD(2024, 1)
    main(aocd)
