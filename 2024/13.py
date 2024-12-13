""" Advent Of Code 2024 : 13 """

from aoctools import *
import numpy as np


def main(aocd: AOCD):
    data = [x.split("\n") for x in aocd.slist_split_at("\n\n")]

    a = 0
    b = 0

    buttons_prizes = []
    for entry in data:
        buttons = []
        x1_inc = int(entry[0].split("X+")[1].split(",")[0])
        y1_inc = int(entry[0].split("Y+")[1])
        x2_inc = int(entry[1].split("X+")[1].split(",")[0])
        y2_inc = int(entry[1].split("Y+")[1])
        buttons.append(np.array([x1_inc, x2_inc]))
        buttons.append(np.array([y1_inc, y2_inc]))
        prize = entry[2]
        x = int(prize.split("X=")[1].split(",")[0])
        y = int(prize.split("Y=")[1])
        buttons_prizes.append([buttons, np.array([x, y])])

    error = 0.01
    c = 10000000000000
    for res in buttons_prizes:
        p1b1, p1b2 = np.linalg.inv(res[0]).dot(res[1])
        p2b1, p2b2 = np.linalg.inv(res[0]).dot(res[1] + c)
        if abs(p1b1 - round(p1b1)) < error and abs(p1b2 - round(p1b2)) < error:
            p1b1, p1b2 = round(p1b1), round(p1b2)
            a += p1b1 * 3 + p1b2
        if abs(p2b1 - round(p2b1)) < error and abs(p2b2 - round(p2b2)) < error:
            p2b1, p2b2 = round(p2b1), round(p2b2)
            b += p2b1 * 3 + p2b2

    aocd.p1(a)
    aocd.p2(b)


if __name__ == "__main__":
    aocd = AOCD(2024, 13)
    main(aocd)
