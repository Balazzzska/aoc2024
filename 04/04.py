import numpy as np

file = "example"
file = "input"

inputlines = open(f"04\\04-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

print(inputlines)

# create a 2d ndarray out of the input
chars = np.array([list(line) for line in inputlines])

print(chars)

WORD = "XMAS"

part1 = 0

print(chars.shape)

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1),
]

for x in range(chars.shape[1]):
    for y in range(chars.shape[0]):
        for dx, dy in directions:
            word = ""
            for i in range(len(WORD)):
                nx = x + i * dx
                ny = y + i * dy
                if nx < 0 or nx >= chars.shape[1] or ny < 0 or ny >= chars.shape[0]:
                    break
                word += chars[ny, nx]
            if word == WORD:
                part1 += 1

print(part1)  # 2583

part2 = 0

for x in range(chars.shape[1]):
    for y in range(chars.shape[0]):
        if x == 0 or y == 0 or x == chars.shape[1] - 1 or y == chars.shape[0] - 1:
            continue

        if chars[y, x] == "A":
            # center of MAS

            UL = chars[y - 1, x - 1]
            UR = chars[y - 1, x + 1]
            BL = chars[y + 1, x - 1]
            BR = chars[y + 1, x + 1]

            tmp = [UL, UR, BL, BR]

            # all must be 'M', or 'S'
            if all(c in "MS" for c in tmp):
                # two of them must be 'M'
                if tmp.count("M") == 2:
                    # diagonals must be different
                    if UL != BR and UR != BL:
                        part2 += 1

print(part2)  # 1978