""" Advent Of Code 2024 : 19 """

from aoctools import *
from functools import cache

def main(aocd: AOCD):
    a = 0
    b = 0

    towels, designs = aocd.slist_split_at("\n\n")
    towels = towels.split(', ')
    designs = designs.split('\n')

    @cache
    def solve(design):
        ways = 0
        if not design:
            ways = 1
        for towel in towels:
            if design.startswith(towel):
                ways += solve(design[len(towel):])
        return ways

    for design in designs:
        if ways := solve(design):
            a += 1
            b += ways

    aocd.p1(a)
    aocd.p2(b)

if __name__ == '__main__':
    aocd = AOCD(2024, 19)
    main(aocd)
