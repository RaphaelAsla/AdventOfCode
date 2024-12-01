""" Advent Of Code 2024 : 1 """

from aoctools import *

def main(aocd: AOCD):
    ml = aocd.imultilist
    aocd.p1(sum(abs(x - y) for x, y in zip(sorted(ml[0]), sorted(ml[1]))))
    aocd.p2(sum(c * ml[1].count(c) for c in ml[0]))

if __name__ == '__main__':
    aocd = AOCD(2024, 1)
    main(aocd)
