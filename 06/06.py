# TODO:
# part2-re volt egy algoritmus ami ca fél óra alatt megoldotta a part2-t.
# elkezdtem optimalizálni, de nem értem a végére. valszeg így is marad örökre :D
from pprint import pprint
import numpy as np
from tqdm import tqdm

file = "example"
# file = "input"

inputlines = open(f"06\\06-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

print(inputlines)

# create a 2d ndarray out of the input
chars = np.array([list(line) for line in inputlines])

# load the map
startpos = None
mapsize = (chars.shape[1], chars.shape[0])
obstacles = []
for y in range(chars.shape[0]):
    for x in range(chars.shape[1]):
        if chars[y, x] == "#":
            obstacles.append((x, y))
        if chars[y, x] == "^":
            startpos = (x, y)

DIRECTIONS = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]


def run_simulation(obstacles_):
    playerdir = DIRECTIONS[0]
    player = startpos
    tail = []
    while (
        player[0] < mapsize[0]
        and player[1] < mapsize[1]
        and player[0] >= 0
        and player[1] >= 0
    ):
        # are we in a loop?
        if ((player, playerdir)) in tail:
            print(f"Loop detected at {player}")

            # calculate the loop length
            loop_length = len(tail) - tail.index((player, playerdir))

            return tail, loop_length

        tail.append((player, playerdir))

        in_front_of_player = (player[0] + playerdir[0], player[1] + playerdir[1])
        if in_front_of_player in obstacles_:
            playerdir = DIRECTIONS[(DIRECTIONS.index(playerdir) + 1) % 4]
            in_front_of_player = (player[0] + playerdir[0], player[1] + playerdir[1])
            # print(f"turning right at {player} to {playerdir}")

        player = in_front_of_player
        # print(f"moving forward to {player}")

    print(f"Out of bounds at {player}")
    return tail, -1


tail, loop_length = run_simulation(obstacles)
unique_tails = set([pos for pos, _ in tail])

print(len(unique_tails))  # 4890

markers = []
# find tails coords where the player has crossed multiple times
for pos in unique_tails:
    crossings = [dir for pos_, dir in tail if pos_ == pos]
    # map direction vectors to idx
    crossings = [DIRECTIONS.index(dir) for dir in crossings]

    if len(crossings) > 1:
        diff = crossings[1] - crossings[0]
        print(diff)
        if diff == -1 or diff == 3 or diff==1:
            crossdir = DIRECTIONS[crossings[1]]
            # right turn
            markers.append((pos[0] + crossdir[0], pos[1] + crossdir[1]))

for y in range(mapsize[1]):
    for x in range(mapsize[0]):
        pos = (x, y)
        char = "░"

        if pos in obstacles:
            char = "█"
        if pos in unique_tails:
            char = "+"
        if pos == startpos:
            char = "▲"
        if pos in markers:
            char = "X"

        print(char, end="")
    print()
