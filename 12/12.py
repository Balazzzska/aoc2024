from pprint import pprint
import numpy as np
from tqdm import tqdm


file = "example"
# file = "example2"
file = "input"

inputlines = open(f"12\\12-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

# create a 2d ndarray out of the input
chars = np.array([list(line) for line in inputlines])

unique_chars = np.unique(chars)
DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]

print(unique_chars)

# create a dictionary with the unique characters as keys and the values as the coordinates of the character
char_dict = {}
for char in unique_chars:
    char_dict[char] = [(p[0], p[1]) for p in np.argwhere(chars == char)]


regions = []
# for char in tqdm(char_dict.keys()):
for char in char_dict.keys():
    print("-----------------" + char)
    gardens = char_dict[char]
    while len(gardens) > 0:
        # get the first point in the list
        point = gardens.pop(0)
        region = [point]
        heads = [point]

        while len(heads) > 0:
            newheads = []
            for head in heads:
                for direction in DIRECTIONS:
                    new_point = (head[0] + direction[0], head[1] + direction[1])
                    if new_point in gardens:
                        gardens.remove(new_point)

                        if new_point not in region:
                            region.append(new_point)
                            newheads.append(new_point)
            heads = newheads

        print(region)
        regions.append(region)


def calculate_perimeter(region):
    perimeter = 0
    for point in region:
        for direction in DIRECTIONS:
            new_point = (point[0] + direction[0], point[1] + direction[1])
            if new_point not in region:
                perimeter += 1
    return perimeter


def calculate_num_sides(region):
    # num sides equals to the number of corners

    num_corners = 0
    for point in region:
        LEFT, RIGHT, UP, DOWN = (
            (point[0] - 1, point[1]),
            (point[0] + 1, point[1]),
            (point[0], point[1] - 1),
            (point[0], point[1] + 1),
        )

        UPLEFT, UPRIGHT, DOWNLEFT, DOWNRIGHT = (
            (point[0] - 1, point[1] - 1),
            (point[0] + 1, point[1] - 1),
            (point[0] - 1, point[1] + 1),
            (point[0] + 1, point[1] + 1),
        )

        if LEFT not in region and UP not in region:
            num_corners += 1
        if RIGHT not in region and UP not in region:
            num_corners += 1
        if LEFT not in region and DOWN not in region:
            num_corners += 1
        if RIGHT not in region and DOWN not in region:
            num_corners += 1

        if DOWN in region and RIGHT in region and DOWNRIGHT not in region:
            num_corners += 1
        if DOWN in region and LEFT in region and DOWNLEFT not in region:
            num_corners += 1
        if UP in region and RIGHT in region and UPRIGHT not in region:
            num_corners += 1
        if UP in region and LEFT in region and UPLEFT not in region:
            num_corners += 1

    return num_corners


def calculate_area(region):
    return len(region)


part1 = 0
part2 = 0
for region in regions:
    part1 += calculate_area(region) * calculate_perimeter(region)
    part2 += calculate_area(region) * calculate_num_sides(region)

    print(region)
    print(calculate_area(region))
    print(calculate_perimeter(region))
    print(calculate_num_sides(region))

print(part1)  # 1464678
print(part2)  # 877492
