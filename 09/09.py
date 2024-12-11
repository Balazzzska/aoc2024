from pprint import pprint

import numpy as np


# file = "example"
# file = "example2"
file = "input"

inputlines = open(f"09\\09-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]
input_str = inputlines[0]

# input_str = "12345"
# input_str = "2333133121414131402"

print(input_str)

# reverse
denseformat = [int(x) for x in input_str]

print(denseformat)

diskmap = np.zeros(sum(denseformat), dtype=int) - 1

# print(diskmap)
n = 0
id = 0
for i, last in enumerate(denseformat):
    if i % 2 == 0:
        diskmap[n : n + last] = id
        id += 1
    else:
        diskmap[n : n + last] = -1
    n += last


# print(diskmap)
# print(len(diskmap))


def printline():
    str_ = "".join([str(x) for x in diskmap])
    str_ = str_.replace("-1", ".")
    print(str_)


printline()

last_id_pos = len(diskmap) - 1
first_empty_pos = denseformat[0]

while last_id_pos > first_empty_pos:
    # print(f"{last_id_pos} > {first_empty_pos}")
    # printline()

    # move to first empty
    diskmap[first_empty_pos] = diskmap[last_id_pos]
    diskmap[last_id_pos] = -1

    # move to next empty
    while diskmap[first_empty_pos] != -1:
        first_empty_pos += 1

    # move to next id
    while diskmap[last_id_pos] == -1:
        last_id_pos -= 1

printline()

part1 = 0
for i, x in enumerate(diskmap):
    x = int(x)  #!!!!!!!!! this is the trick
    if x == -1:
        continue
    part1 += i * x


print(part1)  # 6340197768906
