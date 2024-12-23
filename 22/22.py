import itertools
from pprint import pprint
import numpy as np
from heapq import heappop, heappush

file = "example"
# file = "example2"
file = "input"

inputlines = open(f"22\\22-{file}.txt", "r").readlines()
secret_numbers = [int(line.strip()) for line in inputlines]

pprint(secret_numbers)


def evolve_secret_number(number, num_iterations):
    print(f"Starting with {number}")

    for i in range(num_iterations):
        mul64 = number * 64
        # MIXING; bitwise xor
        number = number ^ mul64
        # PRUNING; modulo 16777216
        number = number % 16777216

        div32 = number // 32
        # MIXING; bitwise xor
        number = number ^ div32
        # PRUNING; modulo 16777216
        number = number % 16777216

        mul2048 = number * 2048
        # MIXING; bitwise xor
        number = number ^ mul2048
        # PRUNING; modulo 16777216
        number = number % 16777216

    print(f"Ending with {number}")
    return number


evolve_secret_number(1, 2000)

part1 = 0
for initial in secret_numbers:
    part1 += evolve_secret_number(initial, 2000)

print(part1)  # 13461553007
