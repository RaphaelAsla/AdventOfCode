""" Advent Of Code 2025 : 7 """

from aoctools import *


def dfs(y, x, grid, memo):
    if not (0 <= y < len(grid) and 0 <= x < len(grid[0])):
        return 1

    if (y, x) in memo:
        return memo[(y, x)]

    cell = grid[y][x]
    if cell == '.':
        res = dfs(y + 1, x, grid, memo)
    elif cell == '^':
        res = dfs(y + 1, x - 1, grid, memo) + dfs(y + 1, x + 1, grid, memo)
    else:
        res = 0

    memo[(y, x)] = res
    return res

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

    memo = {}
    b = dfs(1, inp[0].index('|'), inp, memo)

    aocd.p1(a)
    aocd.p2(b)

if __name__ == '__main__':
    import time
    start = time.time()
    aocd = AOCD(2025, 7)
    main(aocd)
    print(f'Time Taken: {time.time() - start} seconds')
