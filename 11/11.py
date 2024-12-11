from pprint import pprint
import time


stones_ = [125, 17]
stones_ = [int(x) for x in open("11\\11-input.txt", "r").readline().split(" ")]

cache_ = {}


def evolve_stone(val):
    global cache_

    if val in cache_:
        return cache_[val]

    if val == 0:
        res = [1]
    else:
        num_digits = len(str(val))
        if num_digits % 2 == 0:
            res = [
                int(str(val)[: num_digits // 2]),
                int(str(val)[num_digits // 2 :]),
            ]
        else:
            res = [val * 2024]

    cache_[val] = res

    return res


print(stones_)

stones = {}
for stone in stones_:
    if stone in stones:
        stones[stone] += 1
    else:
        stones[stone] = 1

print(stones)

for i in range(75):
    nnn = {}
    for stone in stones.keys():
        ev = evolve_stone(stone)

        for e in ev:
            if e in nnn:
                nnn[e] += stones[stone]
            else:
                nnn[e] = stones[stone]
    stones = nnn

    if i == 24:
        print(sum(stones.values()))  # part1 231278

print(sum(stones.values()))  # part2 274229228071551
