""" Advent Of Code 2025 : 2 """

from aoctools import *


def main(aocd: AOCD):
    inp = [tuple(map(int, s.strip().split('-'))) for s in aocd.slist_split_at(",")]

    a = 0
    b = 0

    for start, end in inp:
        for i in range(start, end + 1):
            s = str(i)
            L = len(s)

            if L % 2 == 0 and s[:L//2] == s[L//2:]:
                a += i

            if L > 1 and len(set(s)) == 1:
                b += i
            else:
                for n in range(2, (L // 2) + 1):
                    if L % n == 0 and all(len(set(s[j::n])) == 1 for j in range(n)):
                        b += i
                        break

    aocd.p1(a)
    aocd.p2(b)

if __name__ == '__main__':
    import time
    start = time.time()
    aocd = AOCD(2025, 2)
    main(aocd)
    print(f'Time Taken: {time.time() - start} seconds')
