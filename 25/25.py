import itertools
from pprint import pprint
import numpy as np
from heapq import heappop, heappush

file = "example"
# file = "example2"
file = "input"

inputlines = open(f"25\\25-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

locks, keys = [], []

i = 0
while i < len(inputlines):
    map_ = np.array([list(line) for line in inputlines[i : i + 7]])

    # print(map_)

    is_lock = map_[0, 0] == "#"  # top row filled then it's a lock

    # count '#' vertically for every row
    heights = np.sum(map_ == "#", axis=0) - 1  # -1 to remove the first row

    if is_lock:
        locks.append(heights)
        print(f"lock; {heights}")
    else:
        keys.append(heights)
        print(f"key; {heights}")

    i += 8

fit = 0
for lock in locks:
    for key in keys:
        heights = lock + key
        if np.all(heights <= 5):
            fit += 1
        pass

print(f"part1: {fit}")  # 3317
