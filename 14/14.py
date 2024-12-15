from pprint import pprint
import re
from matplotlib import pyplot as plt
import numpy as np
import cv2

file, MAP_SIZE = "example", [11, 7]
file, MAP_SIZE = "input", [101, 103]

inputlines = open(f"14\\14-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

positions = []
velocities = []
for line in inputlines:
    # e.g.:p=0,4 v=3,-3
    numbers = [int(x) for x in re.findall(r"[-\d]+", line)]
    print(numbers)

    positions.append(np.array(numbers[:2]))
    velocities.append(np.array(numbers[2:]))

sim_len = 100

# add the velocity sim_len times to the position
positions = np.array(positions)
velocities = np.array(velocities)

velocities = velocities * sim_len
positions = positions + velocities

# modulo with the map size
positions = positions % MAP_SIZE

for y in range(MAP_SIZE[1]):
    for x in range(MAP_SIZE[0]):
        if [x, y] in positions:
            # count the occurence
            cnt = positions.tolist().count([x, y])
            if cnt > 0:
                print(f"{cnt}", end="")
            else:
                print(".", end="")
        else:
            print(".", end="")
    print()


def get_quadrant(x, y):
    if x < MAP_SIZE[0] / 2 - 1 and y < MAP_SIZE[1] / 2 - 1:
        return 1
    elif x > MAP_SIZE[0] / 2 and y < MAP_SIZE[1] / 2 - 1:
        return 2
    elif x < MAP_SIZE[0] / 2 - 1 and y > MAP_SIZE[1] / 2:
        return 3
    elif x > MAP_SIZE[0] / 2 and y > MAP_SIZE[1] / 2:
        return 4
    else:
        return 0  # belongs to no quadrant


quadrant_counts = {}
for p in positions:
    x, y = p
    quadrant = get_quadrant(x, y)

    if quadrant not in quadrant_counts:
        quadrant_counts[quadrant] = 0
    quadrant_counts[quadrant] += 1

for y in range(MAP_SIZE[1]):
    for x in range(MAP_SIZE[0]):
        q = get_quadrant(x, y)
        print(f"{q}", end="")
    print()

for k in sorted(quadrant_counts.keys()):
    print(f"{k}: {quadrant_counts[k]}")


pprint(quadrant_counts.values())


print(
    f"part1: {quadrant_counts[1] * quadrant_counts[2] * quadrant_counts[3] * quadrant_counts[4]}"
)  # 218965032

positions = []
velocities = []
for line in inputlines:
    # e.g.:p=0,4 v=3,-3
    numbers = [int(x) for x in re.findall(r"[-\d]+", line)]
    print(numbers)

    positions.append(np.array(numbers[:2]))
    velocities.append(np.array(numbers[2:]))


positions = np.array(positions)
velocities = np.array(velocities)

# part2
x_variances = []
y_variances = []
for sim in range(100):
    positions = positions + velocities
    positions = positions % MAP_SIZE

    xvariance = np.var(positions[:, 0])
    yvariance = np.var(positions[:, 1])
    x_variances.append(xvariance)
    y_variances.append(yvariance)

    #if xvariance < 600 or yvariance < 600:
    if True:
        bw_image = np.zeros((MAP_SIZE[1], MAP_SIZE[0]), dtype=np.uint8)
        for p in positions:
            x, y = p
            bw_image[y, x] = 255
        # save to bmp
        cv2.imwrite(f"14\\bmps\\{str(sim+1).zfill(5)}.bmp", bw_image)

fig, ax = plt.subplots(nrows=3, ncols=1, sharex=True)
ax[0].plot(x_variances)
ax[1].plot(y_variances)
ax[2].plot([x * y for x, y in zip(x_variances, y_variances)])
plt.show()

# part2 7037
