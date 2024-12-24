import itertools
import json
from pprint import pprint
import numpy as np
from heapq import heappop, heappush

from tqdm import tqdm

file = "example"
file = "input"

inputlines = open(f"23\\23-{file}.txt", "r").readlines()
connections_ = [line.strip() for line in inputlines]

conn = {}
for connection in connections_:
    spl = connection.split("-")
    node1 = spl[0]
    node2 = spl[1]

    if node1 not in conn:
        conn[node1] = set()
    if node2 not in conn:
        conn[node2] = set()

    conn[node1].add(node2)
    conn[node2].add(node1)

triplets = set()
for node1 in conn.keys():
    if not node1.startswith("t"):
        continue

    for node2 in conn[node1]:
        for node3 in conn[node2]:
            if node3 in conn[node1]:
                triplets.add(tuple(sorted((node1, node2, node3))))

# pprint(triplets)

print(f"part1: {len(triplets)}")  # 1119

# p2: find the largest set of computers that are all connected to each other
# Bron–Kerbosch algorithm

largest = set()

# maximal, partial, exluded (R, P, X)
queue = [(set(), set(conn.keys()), set())]
while queue:
    # R, P, X
    maximal, partial, exluded = queue.pop()

    # if P and X are both empty then
    if len(partial) == len(exluded) == 0:
        if len(maximal) > len(largest):
            # report R as a maximal clique
            largest = maximal
            continue

    # for each vertex v in P do...
    for node in list(partial):
        # BronKerbosch1(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
        queue.append((maximal | {node}, partial & conn[node], exluded & conn[node]))

        # P := P \ {v}
        partial = partial - {node}

        # X := X ⋃ {v}
        exluded = exluded | {node}

print(largest)

# av,fr,gj,hk,ii,je,jo,lq,ny,qd,uq,wq,xc
print(",".join([str(x) for x in sorted(largest)]))
