""" Advent Of Code 2025 : 11 """

from aoctools import *
from functools import lru_cache


def main(aocd: AOCD):
    inp = aocd.dict_split_at(': ')

    a = 0
    b = 0 

    tree = {k: v.split() for k, v in inp.items()}

    @lru_cache(None)
    def dfs(node, seen_dac, seen_fft):
        if node == "out":
            return int(seen_dac and seen_fft)

        total = 0
        for nxt in tree.get(node, []):
            total += dfs(nxt, seen_dac or node == "dac", seen_fft or node == "fft")
        return total

    a = dfs("you", True, True)
    b = dfs("svr", False, False)

    aocd.p1(a)
    aocd.p2(b)

if __name__ == '__main__':
    import time
    start = time.time()
    aocd = AOCD(2025, 11)
    main(aocd)
    print(f'Time Taken: {time.time() - start} seconds')
