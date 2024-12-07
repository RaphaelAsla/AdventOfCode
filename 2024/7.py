""" Advent Of Code 2024 : 7 """

from aoctools import *
from itertools import product

def calc(x, eq, p2=False):
    ans = 0
    for ops in product(['+', '*', "||"], repeat=(len(eq) - 1)):
        nxt, *rest = eq
        for i, op in enumerate(ops):
            if op == '+':
                nxt += rest[i]
            elif op == '*':
                nxt *= rest[i]
            elif p2 and op == "||":
                nxt = int(str(nxt) + str(rest[i]))
        if x == nxt:
            ans += nxt
            break
    return ans

def main(aocd: AOCD):
    a = 0
    b = 0

    for x, eq in list(x.split(": ") for x in aocd.slist):
        x = int(x)
        eq = [*map(int, eq.split(' '))]
        a += calc(x, eq, False)
        b += calc(x, eq, True)

    aocd.p1(a)
    aocd.p2(b)

if __name__ == '__main__':
    aocd = AOCD(2024, 7)
    main(aocd)
