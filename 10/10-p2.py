from pprint import pprint
import numpy as np

file = "example2"
file = "input"

inputlines = open(f"10\\10-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

# create a 2d ndarray out of the input
chars = np.zeros((len(inputlines), len(inputlines[0])))
for y, line in enumerate(inputlines):
    for x, char in enumerate(line):
        if char == ".":
            chars[y, x] = -1
        else:
            chars[y, x] = int(char)

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
print(f"startpositions: {startpositions}")

part2 = 0
for startpos in startpositions:
    startpos = tuple(startpos)
    rating = 0

    trails = [[startpos]]

    for i in range(10):
        print(f"-------------------------- # {i}; number of trails: {len(trails)}")
        newtrails = []
        for trail in trails:
            print([chars[pos] for pos in trail])
            head_value = chars[trail[-1]]

            for dir in DIRECTIONS:
                newpos = (trail[-1][0] + dir[0], trail[-1][1] + dir[1])

                # is it in bounds?
                if (
                    newpos[0] < 0
                    or newpos[0] >= chars.shape[0]
                    or newpos[1] < 0
                    or newpos[1] >= chars.shape[1]
                ):
                    continue

                newpos_value = chars[newpos]

                # for debug
                if newpos_value == -1:
                    continue

                if newpos_value - head_value == 1:
                    newtrail = trail.copy()
                    newtrail.append(newpos)

                    # is t in newtrails?
                    already_in = False
                    for t in newtrails:
                        if len(t) == len(newtrail) and all(
                            t[j] == newtrail[j] for j in range(len(t))
                        ):
                            already_in = True
                            break

                    if not already_in:
                        newtrails.append(newtrail)

                        if newpos_value == 9:
                            rating += 1

        trails = newtrails
    print(f"number of trails: {len(trails)}")

    part2 += rating

    print(f"rating: {rating}")

print(part2)  # 1242
