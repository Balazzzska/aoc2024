from pprint import pprint
import numpy as np
from tqdm import tqdm
from heapq import heappop, heappush

file, MAP_SIZE, NUM_BYTES_PART1 = "example", (7, 7), 12
file, MAP_SIZE, NUM_BYTES_PART1 = "input", (71, 71), 1024

inputlines = open(f"18\\18-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

all_corrupted_blocks = []
for line in inputlines:
    x, y = tuple([int(x) for x in line.split(",")])
    all_corrupted_blocks.append((x, y))

for y in range(MAP_SIZE[1]):
    for x in range(MAP_SIZE[0]):
        if (x, y) in all_corrupted_blocks:
            print("#", end="")
        else:
            print(".", end="")
    print()

start = (0, 0)
end = (MAP_SIZE[0] - 1, MAP_SIZE[1] - 1)


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


def solve_maze(block_cnt):
    # find the shortest path from start to end
    # using A star
    open_list = []
    closed_list = set()

    corrupted_blocks = set(all_corrupted_blocks[:block_cnt])

    # (f, pos, g)
    heappush(open_list, (0, start, 0))
    while open_list:
        f, pos, g = heappop(open_list)
        closed_list.add(pos)

        if pos == end:
            # print(f"Found end: {g}")  # 282
            return True, g

        next_positions = get_next_positions(pos)
        for newpos in next_positions:
            if newpos in corrupted_blocks:
                continue

            if newpos in closed_list:
                continue

            new_g = g + 1
            # heuristic, manhattan distance
            h = np.abs(newpos[0] - end[0]) + np.abs(newpos[1] - end[1])
            new_f = new_g + h

            if newpos in [x[1] for x in open_list]:
                continue

            heappush(open_list, (new_f, newpos, new_g))

    return False, -1


# successive binary search
low = 0
high = len(all_corrupted_blocks)

while low < high:
    mid = (low + high) // 2
    print(f"Trying: {mid}... ", end="")
    res, g = solve_maze(mid)
    print(f"Result: {res}, {g}")

    if res:
        low = mid + 1
    else:
        high = mid


print(f"Part 2: {all_corrupted_blocks[low - 1]}")  # 64,29

res, g = solve_maze(NUM_BYTES_PART1)
print(f"Part 1: {res}, {g}")
