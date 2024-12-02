""" Advent Of Code 2024 : 2 """

from aoctools import *

def is_safe(rep):
    inc = rep[0] < rep[1]
    for i in range(len(rep) - 1):
        if not (1 <= abs(rep[i] - rep[i + 1]) <= 3 and (rep[i] < rep[i + 1]) == inc):
            return False, i
    return True, -1 

def tolerable(rep, start):
    return any(is_safe(rep[:i] + rep[i+1:])[0] for i in range(start - 1, len(rep)))

def main(aocd: AOCD):
    a = 0
    b = 0

    for rep in aocd.irows:
        safe, failed_at = is_safe(rep)
        a += safe
        b += safe or tolerable(rep, failed_at) 

    aocd.p1(a)
    aocd.p2(b)

if __name__ == "__main__":
    aocd = AOCD(2024, 2)
    main(aocd)
