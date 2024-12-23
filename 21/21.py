import itertools
from pprint import pprint
import numpy as np
from heapq import heappop, heappush

file = "example"
# file = "example2"
# file = "input"

inputlines = open(f"21\\21-{file}.txt", "r").readlines()
door_codes = [line.strip() for line in inputlines]

print(door_codes)

numeric_keypad = ["789", "456", "123", "#0A"]
numeric_chars = np.array([list(line) for line in numeric_keypad])
directional_keypad = ["#^A", "<v>"]
directional_chars = np.array([list(line) for line in directional_keypad])

print(numeric_chars)
print(directional_chars)


def num_steps_numeric_keypad(from_, to_):
    from_x, from_y = np.where(numeric_chars == from_)
    to_x, to_y = np.where(numeric_chars == to_)
    delta = abs(from_x - to_x) + abs(from_y - to_y)
    return delta[0]


def run_code(code):
    numeric_pos = "A"
    num_steps = 0

    for char in code:
        num_steps += num_steps_numeric_keypad(numeric_pos, char)
        num_steps += 1  # press the button
        numeric_pos = char

    return num_steps


print(run_code("029A"))


print(num_steps_numeric_keypad("1", "9"))
print(num_steps_numeric_keypad("A", "9"))
print(num_steps_numeric_keypad("A", "7"))
