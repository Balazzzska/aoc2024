from pprint import pprint
import numpy as np


# file = "example"
file = "input"

inputlines = open(f"10\\10-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

# create a 2d ndarray out of the input
chars = np.array([list(line) for line in inputlines]).astype(int)

# 2d ndarray of digits
DIRECTIONS = np.array(
    [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0),
    ]
)

pprint(chars)

# where zeroes are
startpositions = np.argwhere(chars == 0)

print(startpositions)
print(DIRECTIONS)

part1 = 0
for startpos in startpositions:
    score = 0
    found_nines = []

    heads = [startpos]
    for i in range(10):
        print(f"-------------------------- # {i}; number of heads: {len(heads)}")

        newheads = []
        for head in heads:
            head_value = chars[tuple(head)]

            print(f"head: {head} value: {head_value}")
            if head_value == 9:
                print("found 9")
                found_nines.append(head)
                continue

            for dir in DIRECTIONS:
                newpos = head + dir

                # is it in bounds?
                if np.any(newpos < 0) or np.any(newpos >= chars.shape):
                    continue

                newpos_value = chars[tuple(newpos)]

                if newpos_value - head_value == 1:
                    # valid next move
                    # print(f"newpos: {newpos} value: {newpos_value}")
                    newheads.append(newpos)

        heads = list(set(map(tuple, newheads)))

    found_nines = list(set(map(tuple, found_nines)))
    score = len(found_nines)

    part1 += score

print(part1)  # 629
