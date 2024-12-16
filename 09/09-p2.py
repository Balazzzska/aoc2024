from pprint import pprint

import numpy as np


# file = "example"
# file = "example2"
file = "input"

inputlines = open(f"09\\09-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]
input_str = inputlines[0]

# input_str = "12345"
input_str = "2333133121414131402"

denseformat = [int(x) for x in input_str]
print(denseformat)

blocks = denseformat[::2]
free_spaces = denseformat[1::2]

print(blocks)
print(free_spaces)


def printmap(df):
    ID = 0
    for i, x in enumerate(df):
        if i % 2 == 0:
            print(str(ID) * x, end="")
            ID += 1
        else:
            print("." * x, end="")
    print()


def printmap2(blocks, spaces):
    a = []
    for b, s in zip(blocks, spaces):
        a.extend([b, s])
    a.append(blocks[-1])
    printmap(a)


printmap(denseformat)
printmap2(blocks, free_spaces)

# grab one block per time and find a suitable space for it
for i, block_size in enumerate(blocks[::-1]):
    block_id = len(blocks) - i - 1

    found = False
    for k, space_size in enumerate(free_spaces):
        if space_size >= block_size:
            # found a space for the block
            found = True
            break

    if not found:
        print("No space found")
        # leave the block as is
    else:
        newblockks = []
        newspaces = []
