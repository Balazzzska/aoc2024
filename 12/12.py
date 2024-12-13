from pprint import pprint
import numpy as np


file = "example"
# file = "input"

inputlines = open(f"12\\12-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

# create a 2d ndarray out of the input
chars = np.array([list(line) for line in inputlines])

unique_chars = np.unique(chars)

print(unique_chars)
