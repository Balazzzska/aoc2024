from heapq import heappop, heappush
import itertools
from pprint import pprint
import numpy as np
from typing import TypeAlias  # trying this for fun

file = "example"
file = "example2"
file = "input"

inputlines = open(f"16\\16-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

# create a 2d ndarray out of the input
chars = np.array([list(line) for line in inputlines])

Vector: TypeAlias = tuple[int, int]
Grid: TypeAlias = dict[Vector, str]
State: TypeAlias = tuple[Vector, Vector]

map: Grid = {(x, y): c for y, line in enumerate(inputlines) for x, c in enumerate(line)}
mapsize = (len(inputlines[0]), len(inputlines))

# find S and E
start = next(k for k, v in map.items() if v == "S")
end = next(k for k, v in map.items() if v == "E")


def get_next_states(state: State):
    (pos_x, pos_y), (vel_x, vel_y) = state

    res = [
        # turn left
        (1000, ((pos_x, pos_y), (vel_y, -vel_x))),
        # turn right
        (1000, ((pos_x, pos_y), (-vel_y, vel_x))),
    ]

    # move forward
    new_pos = (pos_x + vel_x, pos_y + vel_y)
    if map.get(new_pos) != "#":
        res.append((1, (new_pos, (vel_x, vel_y))))

    return res


# lowest cost
costs = {}

start_state = (start, (1, 0))  # facing right
queue = [(0, start_state)]

prev_states = {}

while queue:
    cost, state = heappop(queue)

    pos, _ = state

    if pos == end:
        print("done")
        print(cost)  # 82460
        break

    for weight, next_state in get_next_states(state):
        prev_cost = costs.get(next_state, float("inf"))
        next_cost = cost + weight

        # if we found a better path
        if next_cost < prev_cost:
            costs[next_state] = next_cost
            heappush(queue, (next_cost, next_state))
            prev_states[next_state] = {state}
        elif next_cost == prev_cost:
            # if we found an equally good path
            prev_states[next_state].add(state)

start_node, _ = start_state


def walk(state):
    node, _ = state

    if node == start_node:
        yield [state]
        return
    for prev_state in prev_states[state]:
        for path in walk(prev_state):
            yield path + [state]


paths = list(walk(state))
# pprint(paths)
# print(len(list(paths)))  #

trails = [pos for path in paths for pos, _ in path]

print(len(paths))
print(len(trails))
print(len(set(trails)))  # 590


def printmap():
    for y in range(mapsize[1]):
        for x in range(mapsize[0]):
            if (x, y) in trails:
                print("o", end="")
            else:
                print(map[(x, y)], end="")
        print()


printmap()
