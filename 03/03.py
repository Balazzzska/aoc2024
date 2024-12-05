import numpy as np
import re

file = "example"
file = "example2"
file = "input"

inputlines = open(f"03\\03-{file}.txt", "r").readlines()

part1 = 0
regexp1 = re.compile(r"mul[(]\d{1,3},\d{1,3}[)]")

line = "".join(inputlines)
line = line.strip()
line = regexp1.findall(line)

for match in line:
    m = match.replace("mul(", "")
    m = m.replace(")", "")
    m = m.split(",")
    result = int(m[0]) * int(m[1])
    part1 += result

print(part1)  # 161289189

regexp2 = re.compile(r"mul[(]\d{1,3},\d{1,3}[)]|do[(][)]|don't[(][)]")

line = "".join(inputlines)
line = line.strip()
line = regexp2.findall(line)
part2 = 0
enabled = True
enabled = True
for match in line:
    if match == "do()":
        enabled = True
    elif match == "don't()":
        enabled = False
    else:
        if enabled:
            m = match.replace("mul(", "")
            m = m.replace(")", "")
            m = m.split(",")
            result = int(m[0]) * int(m[1])
            part2 += result
print(part2)  # 83595109
