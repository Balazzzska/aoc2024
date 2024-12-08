import itertools
from pprint import pprint
import numpy as np


file = "example"
# file = "example2"
file = "input"

inputlines = open(f"08\\08-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

print(inputlines)

# create a 2d ndarray out of the input
chars = np.array([list(line) for line in inputlines])

# load the map
mapsize = (chars.shape[1], chars.shape[0])
antennas = {}
for y in range(chars.shape[0]):
    for x in range(chars.shape[1]):
        if chars[y, x] != ".":
            if chars[y, x] not in antennas:
                antennas[chars[y, x]] = []
            antennas[chars[y, x]].append((x, y))

pprint(antennas)
antinodes = []


for frequency in antennas.keys():
    print(f"Frequency {frequency}:")

    # create every possible combination of antennas

    combinations = itertools.combinations(antennas[frequency], 2)

    for pos1, pos2 in combinations:
        print(f"{pos1} <-> {pos2}")
        deltax = pos2[0] - pos1[0]
        deltay = pos2[1] - pos1[1]

        for antinode, DIR in [(pos1, -1), (pos2, 1)]:
            first = True
            while (
                antinode[0] >= 0
                and antinode[0] < mapsize[0]
                and antinode[1] >= 0
                and antinode[1] < mapsize[1]
            ):
                # if not first:
                antinodes.append(antinode)

                antinode = (antinode[0] + deltax * DIR, antinode[1] + deltay * DIR)

                first = False

                # if part1 then break !!!!!!!!!!!!
print(antinodes)

for y in range(mapsize[1]):
    for x in range(mapsize[0]):
        pos = (x, y)

        char = "."
        if pos in antinodes:
            char = "#"

        for frequency in antennas.keys():
            if pos in antennas[frequency]:
                char = frequency

        print(char, end="")
    print()

print(len(set(antinodes)))  # part1; 313
print(len(set(antinodes)))  # part2; 1064
