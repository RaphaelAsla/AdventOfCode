""" Advent Of Code 2025 : 10 """

from aoctools import *
from itertools import combinations
from functools import reduce
from z3 import Int, Sum, Optimize


def main(aocd: AOCD):
    inp = []

    for row in aocd.srows:
        first = [i for i, c in enumerate(row[0][1:-1]) if c == '#']
        middle = [list(map(int, x[1:-1].split(','))) for x in row[1:-1]]
        last = list(map(int, row[-1][1:-1].split(',')))  
        inp.append([first, middle, last])

    a = 0
    b = 0

    for first, middle, last in inp:
        mid_sets = [set(x) for x in middle]
        for k in range(1, len(mid_sets) + 1):
            for combo in combinations(mid_sets, k):
                missing = sorted(reduce(lambda a, b: a ^ b, combo))
                if missing == first:
                    a += k
                    break
            else:
                continue
            break

        press = [Int(f"p{i}") for i in range(len(middle))]
        s = Optimize()
        s.add([p >= 0 for p in press])

        for i in range(len(last)):
            s.add(Sum(press[j] for j, button in enumerate(middle) if i in button) == last[i])

        total_presses = Sum(press)
        s.minimize(total_presses)
        s.check()

        b += int(str(s.model().evaluate(total_presses)))

    aocd.p1(a)
    aocd.p2(b)


if __name__ == '__main__':
    import time
    start = time.time()
    aocd = AOCD(2025, 10)
    main(aocd)
    print(f'Time Taken: {time.time() - start} seconds')
