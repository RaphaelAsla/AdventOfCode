""" Advent Of Code 2025 : 3 """

from aoctools import *


def main(aocd: AOCD):
    inp = aocd.slist

    p1 = 0
    p2 = 0

    for bank in inp:
        mid = bank.index(max(bank))
        left = max(bank[:mid]) if mid > 0 else ''
        right = max(bank[mid+1:]) if mid < len(bank) - 1 else ''
        p1 += max(int(left + bank[mid]), int(bank[mid] + right))

        stack = []
        for pos, digit in enumerate(bank):
            digit = int(digit)
            if not stack:
                stack.append(digit)
            elif stack[-1] >= digit:
                stack.append(digit)
            else:
                while stack and stack[-1] < digit and len(stack) + (len(bank) - pos - 1) >= 12:
                    stack.pop()
                stack.append(digit)
        p2 += int("".join(map(str, stack[:12])))

    aocd.p1(p1)
    aocd.p2(p2)

if __name__ == '__main__':
    import time
    start = time.time()
    aocd = AOCD(2025, 3)
    main(aocd)
    print(f'Time Taken: {time.time() - start} seconds')
