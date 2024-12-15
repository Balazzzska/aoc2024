from pprint import pprint
import numpy as np
from tqdm import tqdm

# file = "example"
file = "input"

inputlines = open(f"15\\15-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

print(inputlines)

# fint the first empty line
for i, line in enumerate(inputlines):
    if line == "":
        break

# create a 2d ndarray out of the first part of the input
chars = np.array([list(line) for line in inputlines[:i]])

# load the map
mapsize = (chars.shape[1], chars.shape[0])
walls = []
boxes = []
robot = None
for y in range(chars.shape[0]):
    for x in range(chars.shape[1]):
        if chars[y, x] == "#":
            walls.append((x, y))
        if chars[y, x] == "O":
            boxes.append((x, y))
        if chars[y, x] == "@":
            robot = (x, y)

# v>^<
DIRECTIONS = {
    "v": (0, 1),
    ">": (1, 0),
    "^": (0, -1),
    "<": (-1, 0),
}


def printmap():
    for y in range(chars.shape[0]):
        for x in range(chars.shape[1]):
            if (x, y) in walls:
                print("#", end="")
            elif (x, y) in boxes:
                print("O", end="")
            elif (x, y) == robot:
                print("@", end="")
            else:
                print(".", end="")
        print()


# load move attempts
moves = inputlines[i + 1 :]
moves = "".join([m.strip() for m in moves])

print(moves)
printmap()

for i, move in enumerate(moves):
    #print("-" * 20)
    #print(f"Move #{i}: {move}")

    dir = DIRECTIONS[move]

    newpos = (robot[0] + dir[0], robot[1] + dir[1])

    if newpos in walls:
        # print("Wall, skip")
        pass
    else:
        if newpos in boxes:
            p = newpos
            while True:
                p = (p[0] + dir[0], p[1] + dir[1])
                if p in walls:
                    break
                if p in boxes:
                    continue
                break

            if p in walls:
                # print("Can't move box, skip")
                pass
            else:
                # print("Move box")
                boxes.remove(newpos)
                boxes.append(p)
                robot = newpos
        else:
            # print("No obstacle, move")
            robot = newpos

printmap()

part1 = 0
for box in boxes:
    part1 += box[1] * 100 + box[0]

print(part1)  # 1485257
