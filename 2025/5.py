""" Advent Of Code 2025 : 5 """

from aoctools import *


def main(aocd: AOCD):
    ranges, ids = [[list(map(int, r.split('-'))) if '-' in r else int(r) for r in x.split('\n')] for x in aocd.slist_split_at('\n\n')]
    ranges = sorted(ranges, key=lambda x: x[0])

    a = 0
    b = 0

    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))

    for id in ids:
        for r in merged:
            if id >= r[0] and id <= r[1]:
                a += 1

    for r in merged:
        b += r[1] - r[0] + 1

    aocd.p1(a)
    aocd.p2(b)

if __name__ == '__main__':
    import time
    start = time.time()
    aocd = AOCD(2025, 5)
    main(aocd)
    print(f'Time Taken: {time.time() - start} seconds')
