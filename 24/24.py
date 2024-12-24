import graphviz
import itertools
import json
from pprint import pprint
import numpy as np
from heapq import heappop, heappush

from tqdm import tqdm

PART2 = True

file = "example"
file = "input"

inputlines = [x.strip() for x in open(f"24\\24-{file}.txt", "r").readlines()]

empty_line_idx = 0
for i, line in enumerate(inputlines):
    if len(line) == 0:
        empty_line_idx = i
        break

# treat inputs as gates
gates = {
    spl[0]: True if int(spl[1]) == 1 else False
    for spl in [line.split(":") for line in inputlines[:empty_line_idx]]
}


# if part2
# Your system of gates and wires has four pairs of gates which need their output wires swapped

wires_to_swap = [("z37", "vkg"), ("z15", "qnw"), ("z20", "cqr"), ("nfj", "ncd")]

allswap = []
for w0, w1 in wires_to_swap:
    allswap.append(w0)
    allswap.append(w1)

p2 = ",".join(sorted(allswap))
# note for my future self:
# no idea how i got here, mostly by
## eyeballing the the generated png,
## and searching for the outputs where the output gate is not XOR
# this is the good answer, im happy, merry xmas :)

print(p2)  # cqr,ncd,nfj,qnw,vkg,z15,z20,z37cqr,ncd,nfj,qnw,vkg,z15,z20,z37

swap = {}
for w0, w1 in wires_to_swap:
    swap[w0] = w1
    swap[w1] = w0


gatelines = inputlines[empty_line_idx + 1 :]
gatelines = list(sorted(gatelines))

# add gates
for line in gatelines:
    spl1 = line.split(" -> ")
    signal_name = spl1[-1].strip()

    if PART2:
        if signal_name in swap:
            signal_name = swap[signal_name]
            print(f"swapping {signal_name} to {swap[signal_name]}")

    spl2 = spl1[0].split(" ")
    operand1 = spl2[0]
    gate_type = spl2[1]
    operand2 = spl2[2]

    gates[signal_name] = (operand1, gate_type, operand2)

not_xor_output = []
for i in range(46):
    xid = "x" + str(i).zfill(2)
    yid = "y" + str(i).zfill(2)
    zid = "z" + str(i).zfill(2)

    if gates[zid][1] != "XOR":
        not_xor_output.append(zid)

pprint(not_xor_output)  # ['z15', 'z20', 'z37', 'z45']

dot = graphviz.Digraph(comment="Circuit")
for signal_name in gates.keys():
    gate = gates[signal_name]
    is_output = signal_name.startswith("z")
    is_input = signal_name.startswith("x") or signal_name.startswith("y")

    label = signal_name

    if not is_input:
        label += f"\n{gate[1]}"

    shape = "ellipse" if signal_name.startswith("z") else "box"

    # fill inputs with colors
    color = "white"
    if signal_name.startswith("x"):
        color = "lightblue"
    elif signal_name.startswith("y"):
        color = "lightgreen"
    elif signal_name.startswith("z"):
        color = "lightcoral"

    if signal_name in not_xor_output:
        color = "red"

    dot.node(
        signal_name,
        label=label,
        shape=shape,
        style="filled",
        fillcolor=color,
    )

    if isinstance(gate, tuple):
        dot.edge(gate[0], signal_name)
        dot.edge(gate[2], signal_name)

dot.render(r"24\24-input.gv", format="png", cleanup=True)


# iterate while gates values have tuples
while any([isinstance(gate, tuple) for gate in gates.values()]):
    # print("iterating...")

    for signal_name, gate in gates.items():
        if isinstance(gate, tuple):
            operand1 = gate[0]
            operand2 = gate[2]

            # substitute operands with values if they are not tuples
            if not isinstance(gates[operand1], tuple):
                operand1 = gates[operand1]
            if not isinstance(gates[operand2], tuple):
                operand2 = gates[operand2]

            # if both operands are bools, calculate the gate value
            if isinstance(operand1, bool) and isinstance(operand2, bool):
                gate_type = gate[1]

                if gate_type == "AND":
                    result = operand1 & operand2
                elif gate_type == "OR":
                    result = operand1 | operand2
                elif gate_type == "XOR":
                    result = operand1 ^ operand2
                else:
                    raise ValueError(f"Unknown gate type: {gate_type}")

                gates[signal_name] = result

zgates = [g for g in gates.keys() if g.startswith("z")]

bin_result = ""
for i in range(len(zgates)):
    # pad to 2 zeroes
    z = gates["z" + str(len(zgates) - i - 1).zfill(2)]
    bin_result += "1" if z else "0"

print(bin_result)

# convert to decimal
if not PART2:
    print(f"p1: {int(bin_result, 2)}")  # 48508229772400
