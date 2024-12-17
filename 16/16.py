import itertools
from pprint import pprint
import numpy as np


file = "example"
file = "example2"
file = "input"

inputlines = open(f"16\\16-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

print(inputlines)

# create a 2d ndarray out of the input
chars = np.array([list(line) for line in inputlines])


DIRECTIONS = {
    0: (0, -1),  # up
    1: (1, 0),  # right
    2: (0, 1),  # down
    3: (-1, 0),  # left
}
print(chars)

for y in range(chars.shape[0]):
    for x in range(chars.shape[1]):
        ccc = chars[y][x]
        if ccc == "S":
            start = (x, y)
        if ccc == "E":
            end = (x, y)

print(start, end)
direction = 1  # right (East)

# (x, y, direction): cost
heads = {(start[0], start[1], direction): 0}

while True:
    # take the head with the smallest cost
    x, y, dir_ = min(heads, key=heads.get)
    cost = heads.pop((x, y, dir_))

    print(len(heads), cost)

    # can we move forward?
    in_front_of_me = (x + DIRECTIONS[dir_][0], y + DIRECTIONS[dir_][1])
    if chars[in_front_of_me[1]][in_front_of_me[0]] == "E":
        print("Found the end!")  # part1 82460
        print(cost + 1)
        break

    if chars[in_front_of_me[1]][in_front_of_me[0]] != "#":
        newhead = (
            in_front_of_me[0],
            in_front_of_me[1],
            dir_,  # same direction
        )
        newcost = cost + 1

        if newhead not in heads or newcost < heads[newhead]:
            heads[newhead] = newcost

    # can we turn left or right?
    for ddd in [(dir_ + 5) % 4, (dir_ + 3) % 4]:
        newpos = (x + DIRECTIONS[ddd][0], y + DIRECTIONS[ddd][1])
        if chars[newpos[1]][newpos[0]] != "#":
            newhead = (
                newpos[0],
                newpos[1],
                ddd,  # new direction
            )
            newcost = cost + 1000 + 1  # new cost

            if newhead not in heads or newcost < heads[newhead]:
                heads[newhead] = newcost
