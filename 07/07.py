import itertools
from pprint import pprint

import numpy as np


file = "example"
file = "input"

inputlines = open(f"07\\07-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines if line.strip() != ""]

print(inputlines)

equations = []
for line in inputlines:
    result = int(line.split(":")[0])
    numbers = [int(x) for x in line.split(": ")[1].split(" ")]
    equations.append((result, numbers))


def concat_operator(x, y):
    ylog10 = int(np.log10(y)) + 1
    x *= 10**ylog10
    return x + y


def could_be_true(equation, part2=False):
    print("-" * 20)
    print(f"Checking {equation}")
    result, numbers = equation

    # generate all possible operator combinations using lambda functions for faster execution
    operators = [
        lambda x, y: x + y,
        lambda x, y: x * y,
    ]

    if part2:
        operators.append(concat_operator)

    for operator_combination in itertools.product(operators, repeat=len(numbers) - 1):
        res = numbers[0]
        for op, n in zip(operator_combination, numbers[1:]):
            res = op(res, n)

        if res == result:
            # write the equation nicely
            equation_str = f"{result} = {numbers[0]}"
            for op, n in zip(operator_combination, numbers[1:]):
                op_str = (
                    "+" if op == operators[0] else "*" if op == operators[1] else "||"
                )
                equation_str += f" {op_str} {n}"
            print(f"Solution found: {equation_str}")
            return True

    print("No solution found")
    return False


part1 = 0
part2 = 0
for equation in equations:
    if could_be_true(equation):
        part1 += equation[0]

    if could_be_true(equation, part2=True):
        part2 += equation[0]

print(part1)  # 3119088655389
print(part2)  # 264184041398847
