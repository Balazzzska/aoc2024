from pprint import pprint
import numpy as np
from tqdm import tqdm


file = "example"
file = "example2"
file = "input"

inputlines = open(f"12\\12-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

# create a 2d ndarray out of the input
chars = np.array([list(line) for line in inputlines])

unique_chars = np.unique(chars)
DIRECTIONS = [
    np.array([0, -1]),
    np.array([1, 0]),
    np.array([0, 1]),
    np.array([-1, 0]),
]

print(unique_chars)

# create a dictionary with the unique characters as keys and the values as the coordinates of the character
char_dict = {}
for char in unique_chars:
    char_dict[char] = [p for p in np.argwhere(chars == char)]


regions = []
for char in tqdm(char_dict.keys()):
    while len(char_dict[char]) > 0:
        print("new region")

        region = []
        region.append(char_dict[char].pop(0))
        head = region.copy()

        changed = True
        while changed:
            changed = False
            for r in region:
                # find if neighbors are in the same region
                for dir in DIRECTIONS:
                    neigh = r + dir
                    if np.any(np.all(neigh == char_dict[char], axis=1)):
                        region.append(neigh)
                        head = [p for p in head if not np.array_equal(p, neigh)]

                        head.append(neigh)

                        char_dict[char] = [
                            p for p in char_dict[char] if not np.array_equal(p, neigh)
                        ]
                        if(len(char_dict[char]) == 0):
                            break
                        changed = True
        regions.append(region)

print(len(regions))
