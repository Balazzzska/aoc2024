import itertools
import json
from pprint import pprint
import numpy as np
from heapq import heappop, heappush

from tqdm import tqdm

file = "example2"
file = "input"

inputlines = open(f"22\\22-{file}.txt", "r").readlines()
secret_numbers = [int(line.strip()) for line in inputlines]


def evolve_secret_number(number, num_iterations):
    best_price_per_sequence = {}

    prev_last_digit = number % 10
    past_4_changes = []

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

        last_digit = number % 10

        past_4_changes.append(last_digit - prev_last_digit)
        if len(past_4_changes) > 4:
            past_4_changes.pop(0)

        if len(past_4_changes) == 4:
            sequence = tuple(past_4_changes)
            if sequence not in best_price_per_sequence:
                best_price_per_sequence[sequence] = 0

            best_price_per_sequence[sequence] = max(
                best_price_per_sequence[sequence], last_digit
            )

        prev_last_digit = last_digit

    return best_price_per_sequence


in_total = {}
for initial in tqdm(secret_numbers):
    best_prices = evolve_secret_number(initial, 2000)

    for sequence, price in best_prices.items():
        if sequence not in in_total:
            in_total[sequence] = 0

        in_total[sequence] += price

# find the max value of dict
max_value = max(in_total.values())
max_key = [k for k, v in in_total.items() if v == max_value]

print(max_key, max_value)  # 1550 too high

# print top 5 values
sorted_dict = sorted(in_total.items(), key=lambda x: x[1], reverse=True)
print(sorted_dict[:5])  # 1529, second best too high
