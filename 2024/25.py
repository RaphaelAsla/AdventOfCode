""" Advent Of Code 2024 : 25 """

from aoctools import *

def main(aocd: AOCD):
    a = 0

    entries = aocd.slist_split_at("\n\n")

    locks = []
    keys = []

    for entry in entries:
        m = entry.split('\n')
        temp = [sum(1 for y in range(len(m)) if m[y][x] == '#') - 1 for x in range(len(m[0]))]
        (locks if m[0][0] == '#' else keys).append(temp)

    a = sum(1 for lock in locks for key in keys if all((a + b) <= 5 for a, b in zip(lock, key)))

    aocd.p1(a)

if __name__ == '__main__':
    aocd = AOCD(2024, 25)
    main(aocd)
