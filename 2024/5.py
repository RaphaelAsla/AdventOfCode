""" Advent Of Code 2024 : 5 """

from aoctools import *
from collections import defaultdict

def main(aocd: AOCD):
    a = 0
    b = 0

    rules, updates = [x.split('\n') for x in aocd.slist_split_at("\n\n")]

    updates = [update.split(',') for update in updates]

    before = defaultdict(list)
    for x, y in [rule.split('|') for rule in rules]:
        before[y].append(x)

    for update in updates:
        sorted = True
        for _ in range(len(update) // 2 + 1):
            for i in range(len(update) - 1, 0, -1):
                for j in range(i):
                    if update[j] not in before[update[i]]:
                        update.append(update.pop(j))
                        sorted = False
            if sorted:
                a += int(update[len(update) // 2])
                break
        if not sorted:
            b += int(update[len(update) // 2])

    aocd.p1(a)
    aocd.p2(b)

if __name__ == '__main__':
    aocd = AOCD(2024, 5)
    main(aocd)
