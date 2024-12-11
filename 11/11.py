import time


stones = [125, 17]

# stones = [int(x) for x in open("11\\11-input.txt", "r").readline().split(" ")]


def evolve_stone(val):
    if val == 0:
        return [1]
    else:
        num_digits = len(str(val))
        if num_digits % 2 == 0:
            return [
                int(str(val)[: num_digits // 2]),
                int(str(val)[num_digits // 2 :]),
            ]
        else:
            return [val * 2024]


print(stones)


stonedict = {}
for stone in stones:
    if stone in stonedict:
        stonedict[stone] += 1
    else:
        stonedict[stone] = 1



start_time = time.time()
for i in range(10):
    # print(f"{i},{time.time() - start_time:.3f}")

    newstones = []
    for stone in stones:
        newstones += evolve_stone(stone)
    stones = newstones
    print(stones)

    if i == 24:
        print(f"part 1: {len(stones)}")  # 231278

print(len(stones))
