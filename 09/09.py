from pprint import pprint

import numpy as np


# file = "example"
# file = "example2"
file = "input"

inputlines = open(f"09\\09-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]
input_str = inputlines[0]

# input_str = "12345"
# input_str = "2333133121414131402"

print(input_str)

# reverse
denseformat = [int(x) for x in input_str][::-1]

print(denseformat)

diskmap = np.zeros(sum(denseformat), dtype=int)

print(diskmap)

skip = False
n = 0
id = 1
while len(denseformat) > 0:
    last = denseformat.pop()
    if skip:
        skip = False
        n += last
    else:
        diskmap[n : n + last] = id
        id += 1
        n += last
        skip = True

print(diskmap)

print(len(diskmap))

