"""Advent Of Code 2025 : 6"""

from aoctools import *
from itertools import groupby
from math import prod


def main(aocd: AOCD):
    inp = aocd.slist_split_at("\n")
    nums = [list(map(int, line.split())) for line in inp[:-1]]
    syms = inp[-1].split()

    a = 0
    b = 0

    for i in range(len(nums[0])):
        values = [int(row[i]) for row in nums if row[i]]
        a += prod(values) if syms[i] == "*" else sum(values)

    nums = [list(line) for line in inp[:-1]]

    it = ["".join(row[x] for row in nums if row[x].isdigit()) for x in range(len(nums[0]))]
    prob = [list(map(int, group)) for k, group in groupby(it, key=lambda x: x != "") if k]

    b += sum(prod(v) if syms[i] == "*" else sum(v) for i, v in enumerate(prob))

    aocd.p1(a)
    aocd.p2(b)


if __name__ == "__main__":
    import time

    start = time.time()
    aocd = AOCD(2025, 6)
    main(aocd)
    print(f"Time Taken: {time.time() - start} seconds")
