""" Advent Of Code 2024 : 9 """

from aoctools import *

def main(aocd: AOCD):
    a = 0
    b = 0

    disk_map = list(map(int, aocd.as_str))

    flatten_blocks = sum([[-1 if i % 2 else i // 2] * int(n) for (i, n) in enumerate(disk_map)], [])

    left = 0
    right = len(flatten_blocks) - 1

    while left <= right:
        if flatten_blocks[left] == -1 and flatten_blocks[right] != -1:
            flatten_blocks[right], flatten_blocks[left] = flatten_blocks[left], flatten_blocks[right]
            left += 1
            right -= 1
        elif flatten_blocks[right] == -1:
            right -= 1
        elif flatten_blocks[left] != -1:
            left += 1

    a = sum([i * num for i, num in enumerate(flatten_blocks) if num > 0])

    space = []
    blocks = []
    idx = 0
    for i, l in enumerate(disk_map):
        if i % 2:
            space.append((idx, l))
        else:
            blocks.append((idx, l))
        idx += l

    for i, block in [*enumerate(blocks)][::-1]: 
        for j, fs in enumerate(space):        
            if fs[0] < block[0] and fs[1] >= block[1]:          
                blocks[i] = (fs[0], block[1])
                space[j] = (fs[0] + block[1], fs[1] - block[1])
                break

    b = sum(i * v for v, (idx, blen) in enumerate(blocks) for i in range(idx, idx + blen))

    aocd.p1(a)
    aocd.p2(b)

if __name__ == '__main__':
    aocd = AOCD(2024, 9)
    main(aocd)
