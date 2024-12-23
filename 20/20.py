import itertools
from pprint import pprint
import numpy as np
from heapq import heappop, heappush

file = "example"
# file = "example2"
file = "input"

inputlines = open(f"20\\20-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

# create a 2d ndarray out of the input
chars = np.array([list(line) for line in inputlines])

MAP_SIZE = (chars.shape[1], chars.shape[0])
print(chars)
walls = set()

for y in range(chars.shape[0]):
    for x in range(chars.shape[1]):
        ccc = chars[y][x]

        if ccc == "#":
            walls.add((x, y))
        if ccc == "S":
            start = (x, y)
        if ccc == "E":
            end = (x, y)


def get_next_positions(pos):
    x, y = pos

    res = []
    for newpos in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if newpos[0] < 0 or newpos[0] >= MAP_SIZE[0]:
            continue
        if newpos[1] < 0 or newpos[1] >= MAP_SIZE[1]:
            continue
        res.append(newpos)
    return res


print(start, end)

# A star algorithm


open_list = []
closed_list = set()
parents = {}  # to reconstruct the path


# (f, pos, g)
heappush(open_list, (0, start, 0))

while open_list:
    f, pos, g = heappop(open_list)
    closed_list.add(pos)

    if pos == end:
        print(f"Found end: {g}")

        # reconstruct the path
        path = []
        while pos != start:
            path.append(pos)
            pos = parents[pos]
        path.append(start)
        path.reverse()

        break

    next_positions = get_next_positions(pos)
    for next_pos in next_positions:
        if next_pos in walls:
            continue
        if next_pos in closed_list:
            continue

        new_g = g + 1
        new_f = new_g + abs(next_pos[0] - end[0]) + abs(next_pos[1] - end[1])

        parents[next_pos] = pos
        heappush(open_list, (new_f, next_pos, new_g))

print(path)

for y in range(MAP_SIZE[1]):
    for x in range(MAP_SIZE[0]):
        if (x, y) in path:
            print(".", end="")
        elif (x, y) in walls:
            print("#", end="")
        else:
            print(" ", end="")
    print()

cnt_ = {}
for idx, (x, y) in enumerate(path):
    for in_between, cheat_pos in zip(
        [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)],
        [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)],
    ):
        if cheat_pos in walls:
            continue

        if cheat_pos in path and in_between not in path:
            idx2 = path.index(cheat_pos)
            delta = idx2 - idx
            delta -= 2  # ???
            if delta > 0:
                if delta not in cnt_:
                    cnt_[delta] = 0

                cnt_[delta] += 1

at_least_100 = 0
for k in sorted(cnt_.keys()):
    print(cnt_[k], k)
    if k >= 100:
        at_least_100 += cnt_[k]

print(at_least_100)  # 1404
