""" Advent Of Code 2024 : 17 """

from aoctools import *


def main(aocd: AOCD):
    register, program = aocd.slist_split_at('\n\n')
    A, B, C = map(int, [reg.split(': ')[1] for reg in register.split('\n')])
    program = [int(x) for x in program.split(':')[1].split(',')]

    out = []
    i = 0
    while i < len(program):
        combo = program[i + 1]
        if combo == 4:
            combo = A
        elif combo == 5:
            combo = B
        elif combo == 6:
            combo = C
        if program[i] == 0:
            A //= 2**combo
        elif program[i] == 1:
            B ^= program[i + 1]
        elif program[i] == 2:
            B = combo % 8
        elif program[i] == 3 and A != 0:
            i = combo - 2
        elif program[i] == 4:
            B ^= C
        elif program[i] == 5:
            out.append(combo % 8)
        elif program[i] == 6:
            B = A // 2**combo
        elif program[i] == 7:
            C = A // 2**combo
        i += 2

    a = ','.join(map(str, out))

    aocd.p1(a)

if __name__ == '__main__':
    aocd = AOCD(2024, 17)
    main(aocd)
