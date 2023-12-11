import numpy as np
import re
"""
The pipes are arranged in a two-dimensional grid of tiles:

| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""

PIPE_DICT = {"S": (0, 0),
             "|": [(-1, 0), (+1, 0)],
             "-": [(0, -1), (0, +1)],
             "L": [(-1, 0), (0, +1)],
             "J": [(0, -1), (-1, 0)],
             "7": [(0, -1), (1, 0)],
             "F": [(1, 0), (0, 1)]}


# test_input = """-L|F7
# 7S-7|
# L|7||
# -L-J|
# L|-JF"""

# test_input = """..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ..."""

test_input = """.....
.S-7.
.|.|.
.L-J.
....."""


def input_parser(test_input):
    text_inputs = test_input.split('\n')

    idx = re.search(r"[S]", "".join(text_inputs)).span()
    nrow, ncol = len(text_inputs), len(text_inputs[0])
    symbol_pattern = r"[|LJ7F\-S]"
    mask = np.full((nrow, ncol), -1)

    for i, line in enumerate(text_inputs):
        for msym in re.finditer(symbol_pattern, line):
            start, end = msym.span()
            mask[i, start:end] = 1

    return [list(line) for line in text_inputs], idx, mask


PIPES, idx, MASK = input_parser(test_input)
# with open("data/day9.txt", "r") as file:
# SIGNALS = input_parser(file.read())

print(PIPES)

start_idx = (int(idx[0] / len(PIPES[0])), idx[0] % len(PIPES[0]))
print(start_idx)

neig_indexes = np.array([[0, -1], [-1, 0], [0, 1], [1, 0]]) + start_idx

neighbours = [PIPES[n_idx[0]][n_idx[1]] for n_idx in neig_indexes]


for n_idx, neigh in zip(neig_indexes, neighbours):
    if neigh != ".":
        rev_start = sum((n_idx + PIPE_DICT[neigh][0]) - start_idx)
        rev_start1 = sum((n_idx + PIPE_DICT[neigh][1]) - start_idx)
        print(n_idx, neigh, rev_start, rev_start1)
        if rev_start == 0:
            MASK[n_idx] = MASK[n_idx] + 1
        # if rev_start1 == 0:


print(MASK)
