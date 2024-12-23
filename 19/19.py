from pprint import pprint
import numpy as np
from tqdm import tqdm
from heapq import heappop, heappush

file = "example"
file = "input"

inputlines = open(f"19\\19-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

patterns_ = [x.strip() for x in inputlines[0].split(",")]
patterns = {}
for pattern in patterns_:
    first_char = pattern[0]

    if first_char not in patterns:
        patterns[first_char] = []

    patterns[first_char].append(pattern)

print(patterns)

designs = [x.strip() for x in inputlines[2:]]

print(designs)


def is_valid_design(design):
    queue = [(0, [])]

    while queue:
        idx, hist = queue[-1]
        queue = queue[:-1]

        curr = "".join(hist)

        if curr == design:
            return True

        if idx >= len(design):
            continue

        nextchar = design[idx]
        if nextchar not in patterns:
            continue

        for prefix in patterns[nextchar]:
            len_ = len(prefix)

            if design[idx : idx + len_] != prefix:
                continue
            item = (idx + len_, hist + [prefix])

            if item in queue:
                continue

            queue.append(item)

    return False  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# q = is_valid_design("bwurrg")
# print(q)
# exit()

validcnt = 0
for i, design in enumerate(designs):
    is_valid = is_valid_design(design)
    if is_valid:
        print(f"{i} is valid")
        validcnt += 1
    else:
        print(f"{i} is invalid")

print(f"part1 {validcnt}")  # 285

