import numpy as np

file = "example"
file = "input"

filecontents = open(f"01\\01-{file}.txt", "r")
filecontents = [r.replace("   ", " ") for r in filecontents]

input_data = np.loadtxt(filecontents, dtype=int)

left = input_data[:, 0]
right = input_data[:, -1]

part1 = np.sum(np.abs(np.sort(right) - np.sort(left)))
print(part1)

part2 = 0
for l in left:
    part2 += np.count_nonzero(right == l) * l

print(part2)
