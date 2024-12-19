from pprint import pprint
import numpy as np
from tqdm import tqdm
from heapq import heappop, heappush

# file = "example"
file = "input"

inputlines = open(f"19\\19-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

patterns = [x.strip() for x in inputlines[0].split(",")]

print(patterns)

designs = [x.strip() for x in inputlines[2:]]

print(designs)



def is_valid_design(design):

    # print(f"Checking {design}")

    to_check = []
    for pattern in patterns:
        # if design starts with pattern
        if design.startswith(pattern):
            to_check.append(pattern)

    # print(f"to_check {to_check}")

    if len(to_check) == 0:
        return False

    chopped = [design[len(pattern) :] for pattern in to_check]

    # if any is zero then we are done
    if any([len(c) == 0 for c in chopped]):
        return True

    res = [is_valid_design(c) for c in chopped]

    return any(res)


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

print(f"part1 {validcnt}")
