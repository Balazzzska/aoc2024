import itertools
from pprint import pprint
import numpy as np


file = "example"
# file = "example2"
# file = "input"

inputlines = open(f"16\\16-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

print(inputlines)

# create a 2d ndarray out of the input
chars = np.array([list(line) for line in inputlines])

print(chars)
