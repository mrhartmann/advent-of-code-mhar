import numpy as np
import re
import itertools

test_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

EXPANSION_FACTOR = int(2)


def dist(a, b):
    return sum(np.abs(b-a))


def expansion_dist(galaxy_locs, exp_rows, exp_cols):
    """For part two"""
    summer = 0
    for subset in itertools.combinations(galaxy_locs, 2):
        a, b = subset[0], subset[1]
        ax_index = np.searchsorted(exp_rows, a[0])
        ay_index = np.searchsorted(exp_cols, a[1])
        bx_index = np.searchsorted(exp_rows, b[0])
        by_index = np.searchsorted(exp_cols, b[1])

        if ax_index == bx_index and a[0] < exp_rows[ax_index]:
            bx_index += 1
        if ay_index == by_index:
            by_index += 1

        print(a, b)
        print("Indexes: ", ax_index, bx_index, ay_index, by_index)
        print("Val at indexes: ", exp_rows[ax_index],
              exp_rows[bx_index], exp_cols[ay_index], exp_cols[by_index])
        print(exp_rows[ax_index:bx_index], exp_cols[ay_index:by_index], "\n")

        summer += dist(a, b)

        exp_ordinals_passed = len(
            exp_rows[ax_index:bx_index]) + len(exp_cols[ay_index:by_index])

        summer += EXPANSION_FACTOR * exp_ordinals_passed
        print(summer)

    return summer


def parse_mask(text_input, insert=True):
    """Find all digits positions in the input lines
    by length of number get the neighborhood filter
    Create a matrix that represents all the number and symbol positions
    and at each number position check the neighborhood for symbols"""
    text_inputs = text_input.split("\n")
    nrow, ncol = len(text_inputs), len(text_inputs[0])
    symbol_pattern = r"[\#]"
    mask = np.zeros(shape=(nrow, ncol))

    match_count = 1
    for i, line in enumerate(text_inputs):
        for msym in re.finditer(symbol_pattern, line):
            # print(i, msym.span())
            start, end = msym.span()
            mask[i, start:end] = match_count
            match_count += 1

    print(f"Mask shape before: {mask.shape}")
    zero_cols = np.where(~mask.any(axis=0))[0]
    zero_rows = np.where(~mask.any(axis=1))[0]

    print("Expanding following rows and cols: ", zero_rows, zero_cols)
    if insert:

        mask = np.insert(mask, zero_rows, 0, axis=0)
        mask = np.insert(mask, zero_cols, 0, axis=1)
        print(f"Mask shape after expansion: {mask.shape}")

    return mask, zero_rows, zero_cols


# MASK, ZERO_ROWS, ZERO_COLS = parse_mask(test_input)
with open("data/day11.txt", "r") as file:
    MASK, ZERO_ROWS, ZERO_COLS = parse_mask(file.read())
print(MASK, MASK.shape)


galaxy_locs = np.array(np.where(MASK != 0)).T

summer = 0
for subset in itertools.combinations(galaxy_locs, 2):
    summer += dist(*subset)

print("Result PART 1: ", summer)


print("\n\nPART TWO: ")
MASK, ZERO_ROWS, ZERO_COLS = parse_mask(test_input, insert=False)
print(MASK, MASK.shape)

# with open("data/day11.txt", "r") as file:
#     MASK, ZERO_ROWS, ZERO_COLS = parse_mask(file.read(), insert=False)

galaxy_locs = np.array(np.where(MASK != 0)).T
summer_2nd_part = expansion_dist(galaxy_locs, ZERO_ROWS, ZERO_COLS)

print("Result PART 2: ", summer_2nd_part)
