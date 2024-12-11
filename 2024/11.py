""" Advent Of Code 2024 : 11 """

from aoctools import *
from functools import cache

@cache
def solve(stone, t):
    if t == 0:
        return 1
    elif stone == 0:
        return solve(1, t - 1)
    elif len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        mid = len(str_stone) // 2
        left = int(str_stone[:mid])
        right = int(str_stone[mid:])
        return solve(left, t - 1) + solve(right, t - 1)
    return solve(stone * 2024, t - 1)

def main(aocd: AOCD):
    stones = aocd.ilist_split_at(" ")

    a = sum(solve(stone, 25) for stone in stones)
    b = sum(solve(stone, 75) for stone in stones)

    aocd.p1(a)
    aocd.p2(b)

if __name__ == "__main__":
    aocd = AOCD(2024, 11)
    main(aocd)
