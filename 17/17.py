from pprint import pprint
import numpy as np
from tqdm import tqdm

file = "example"
file = "example2"
file = "input"

inputlines = open(f"17\\17-{file}.txt", "r").readlines()
inputlines = [line.strip() for line in inputlines]

registers = {}  # "A", "B", "C"

for i in range(3):
    line = inputlines[i]
    spl = line.split(":")
    registers[spl[0][-1]] = int(spl[1])

#registers["A"] = 555555555555555
registers["A"] = 111
print(registers)


program = [int(x) for x in inputlines[4].split(":")[-1].split(",")]

print(program)

instruction_pointer = 0

# opcodes having literal operands
literal_operands = [1, 3]

output = []
cnt = 0

opcode_names = {
    0: "ADV",
    1: "XOR",
    2: "MOD",
    3: "JNZ",
    4: "XOR",
    5: "OUT",
    6: "BDV",
    7: "CDV",
}
while True:
    cnt += 1

    if instruction_pointer >= len(program):
        break

    opcode = program[instruction_pointer]
    operand = program[instruction_pointer + 1]

    print("-" * 20)
    print(f"Instruction pointer: {instruction_pointer}; Registers: {registers}")
    print(f"Opcode: {opcode} [{opcode_names[opcode]}] ; Operand: {operand}")

    if opcode not in literal_operands:
        # not literal, combo operands
        if operand in [0, 1, 2, 3]:
            # nothing to do
            pass
        elif operand == 4:
            operand = registers["A"]
        elif operand == 5:
            operand = registers["B"]
        elif operand == 6:
            operand = registers["C"]
        else:
            print("Unknown operand", operand)
            break
        print(f"Operand combo: {operand}")

    if opcode == 0:
        # adv
        print(f"ADV; Dividing A by 2^{operand}, putting result in A")
        registers["A"] = int(registers["A"] / (2**operand))
    elif opcode == 1:
        # bitwise xor
        print(f"XORing B with {operand}, putting result in B")
        registers["B"] = registers["B"] ^ operand
    elif opcode == 2:
        # modulo 8
        print(f"Modulo 8 of {operand}, putting result in B")
        registers["B"] = operand % 8
    elif opcode == 3:
        # "JNZ"
        print(f"Jumping to {operand} if A is not 0")
        if registers["A"] == 0:
            pass
        else:
            print("Jumping...")
            instruction_pointer = operand
            continue
    elif opcode == 4:
        # bitwise xor
        print("XORing B with C, putting result in B")
        registers["B"] = registers["B"] ^ registers["C"]
    elif opcode == 5:
        # "out"
        operand = operand % 8
        print(f"Output: {operand}")
        output.append(operand)
    elif opcode == 6:
        # bdv
        print(f"BDV; Dividing A by 2^{operand}, putting result in B")
        registers["B"] = int(registers["A"] / (2**operand))
    elif opcode == 7:
        # cdv
        print(f"CDV; Dividing A by 2^{operand}, putting result in C")
        registers["C"] = int(registers["A"] / (2**operand))

    instruction_pointer += 2

print("Cycle count:", cnt)
print(",".join([str(x) for x in output]))