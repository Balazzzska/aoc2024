import numpy as np

file = "example"
file = "input"

lines = open(f"02\\02-{file}.txt", "r")


def is_line_safe(values):
    diff = np.diff(values)
    if np.all(diff > 0):
        return np.count_nonzero(diff >= 4) == 0
    elif np.all(diff < 0):
        return np.count_nonzero(diff <= -4) == 0
    return False


part1 = 0
part2 = 0
for line in lines:
    line = line.split(" ")
    line = np.array(line, dtype=int)

    if is_line_safe(line):
        part1 += 1

    for i in range(len(line)):
        # skit ith element
        line_without_i = np.delete(line, i)

        if is_line_safe(line_without_i):
            part2 += 1
            break

print(part1)  # 421
print(part2)  # 476
