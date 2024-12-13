from scipy.optimize import linprog
from pprint import pprint
import numpy as np
import re

file = "example"
file = "input"
PART2 = True

inputlines = open(f"13\\13-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines if line.strip() != ""]
numbers = [re.findall(r"\d+", line) for line in inputlines]

print(numbers)


part1 = 0
for i in range(len(numbers) // 3):
    button_a = int(numbers[i * 3][0]), int(numbers[i * 3][1])
    button_b = int(numbers[i * 3 + 1][0]), int(numbers[i * 3 + 1][1])
    target = int(numbers[i * 3 + 2][0]), int(numbers[i * 3 + 2][1])

    print("-" * 80)
    print(f"button_a: {button_a}; button_b: {button_b}; target: {target}")

    if PART2:
        target = (
            10000000000000 + target[0],
            10000000000000 + target[1],
        )

    # A*Ax + B*Bx = Tx
    # A*Bx + B*By = Ty

    Ax = button_a[0]
    Ay = button_a[1]
    Bx = button_b[0]
    By = button_b[1]
    Tx = target[0]
    Ty = target[1]

    # Cramer's rule

    determinant = Ax * By - Ay * Bx
    A = (Tx * By - Ty * Bx) / determinant
    B = (Ax * Ty - Ay * Tx) / determinant

    A = int(A)
    B = int(B)

    print(f"ASD: {(Ax * A + Bx * B, Ay * A + By * B)}")
    if (Ax * A + Bx * B, Ay * A + By * B) == (target[0], target[1]):
        print(f"A: {A}; B: {B}")
        part1 += 3 * A + B
    else:
        print("no solution")

    # ONLY BRUTE FORCE LIES AHEAD
    continue

    heads = {(0, 0): 0}  # x,y:coins spent

    solutions = []

    while len(heads) > 0:
        newheads = {}
        for (x, y), coins in heads.items():
            for (dx, dy), cost in [(button_a, 3), (button_b, 1)]:
                newx = x + dx
                newy = y + dy
                newcost = coins + cost

                if newx > target[0] or newy > target[1]:
                    continue

                if newx == target[0] and newy == target[1]:
                    solutions.append(newcost)
                    continue

                # is this already in the list?
                # if yes, check if the cost is lower

                if (newx, newy) in newheads:
                    if newcost < newheads[(newx, newy)]:
                        newheads[(newx, newy)] = newcost
                else:
                    newheads[(newx, newy)] = newcost

        heads = newheads

    if len(solutions) == 0:
        print("no solutions")
    else:
        print(solutions)
        part1 += min(solutions)

print(part1)  # 35729
