""" Advent Of Code 2024 : 3 """

from aoctools import *
import re

def main(aocd: AOCD):
    a = 0
    b = 0

    a = sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", aocd.as_str))
    b = sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", re.sub(r"don\'t\(\).*?(?=do\(\))|don\'t\(\).*", "", aocd.as_str.replace('\n', ''))))

    aocd.p1(a)
    aocd.p2(b)

if __name__ == '__main__':
    aocd = AOCD(2024, 3)
    main(aocd)
