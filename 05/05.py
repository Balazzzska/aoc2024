file = "example"
file = "input"

inputlines = open(f"05\\05-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines if line.strip() != ""]

rules = [line for line in inputlines if "|" in line]
manuals = [line for line in inputlines if "," in line]

rules = [list(map(int, line.split("|"))) for line in rules]
manuals = [list(map(int, line.split(","))) for line in manuals]

print(rules)
print(manuals)


def validate(manual):
    for rule in rules:
        if rule[0] in manual and rule[1] in manual:
            idx_0 = manual.index(rule[0])
            idx_1 = manual.index(rule[1])

            if idx_0 > idx_1:
                return False

    return True


part1 = 0
part2 = 0
for manual in manuals:
    is_valid = validate(manual)

    if is_valid:
        mid_number = manual[len(manual) // 2]
        part1 += mid_number
    else:
        print(f"invalid: {manual}")
        while not validate(manual):
            for rule in rules:
                if rule[0] in manual and rule[1] in manual:
                    idx_0 = manual.index(rule[0])
                    idx_1 = manual.index(rule[1])

                    if idx_0 > idx_1:
                        # swap
                        manual[idx_0], manual[idx_1] = manual[idx_1], manual[idx_0]
        print(f"VALID  : {manual}")
        mid_number = manual[len(manual) // 2]
        part2 += mid_number


print(part1)  # 5166
print(part2)  # 4679
