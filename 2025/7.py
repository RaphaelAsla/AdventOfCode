""" Advent Of Code 2025 : 7 """

from aoctools import *
from functools import lru_cache


def main(aocd: AOCD):
    inp = [list(r.replace('S', '|')) for r in aocd.slist_split_at('\n')]

    a = 0
    b = 0

    for y, row in enumerate(inp):
        for x, c in enumerate(row):
            if c == '|':
                if y < len(inp) - 1:
                    under = inp[y + 1]
                    if under[x] == '^':
                        under[x-1:x+2:2] = ['|', '|']
                        a += 1
                    else:
                        under[x] = '|'

    inp = [inp[0]] + [['.' if c == '|' else c for c in row] for row in inp[1:]]

    @lru_cache(None)
    def dfs(y, x):
        if not (0 <= y < len(inp) and 0 <= x < len(inp[0])):
            return 1

        cell = inp[y][x]
        if cell == '.':
            return dfs(y + 1, x)
        elif cell == '^':
            return dfs(y + 1, x - 1) + dfs(y + 1, x + 1)
        else:
            return 0

    b = dfs(1, inp[0].index('|'))

    aocd.p1(a)
    aocd.p2(b)

if __name__ == '__main__':
    import time
    start = time.time()
    aocd = AOCD(2025, 7)
    main(aocd)
    print(f'Time Taken: {time.time() - start} seconds')
