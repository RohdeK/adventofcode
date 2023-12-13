import math
from typing import List

from puzzles.day_13.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import PlanarMap


def find_mirror_cols(mirror: PlanarMap) -> List[float]:
    mirrors_found = []

    mirror_options = [m + 0.5 for m in mirror.col_indices()[:-1]]
    for mirror_col in mirror_options:
        mirror_impossible = False
        num_diffs = 0

        for orig_col in mirror.col_indices():
            if orig_col > mirror_col:
                continue

            copy_col = int(2 * mirror_col - orig_col)

            if copy_col not in mirror.tiles_by_col:
                continue

            orig_types = [t.type for t in mirror.tiles_by_col[orig_col]]
            copy_types = [t.type for t in mirror.tiles_by_col[copy_col]]

            col_diffs = sum(1 for o, c in zip(orig_types, copy_types) if o != c)

            num_diffs += col_diffs

            if num_diffs > 1:
                mirror_impossible = True
                break

        if num_diffs == 0:
            print("Found proper mirror at col", mirror_col)
            mirror_impossible = True

        if not mirror_impossible:
            mirrors_found.append(mirror_col)

    return mirrors_found


def find_mirror_rows(mirror: PlanarMap) -> List[float]:
    mirrors_found = []

    mirror_options = [m + 0.5 for m in mirror.row_indices()[:-1]]
    for mirror_row in mirror_options:
        mirror_impossible = False
        num_diffs = 0

        for orig_row in mirror.row_indices():
            if orig_row > mirror_row:
                continue

            copy_row = int(2 * mirror_row - orig_row)

            if copy_row not in mirror.tiles_by_row:
                continue

            orig_types = [t.type for t in mirror.tiles_by_row[orig_row]]
            copy_types = [t.type for t in mirror.tiles_by_row[copy_row]]

            col_diffs = sum(1 for o, c in zip(orig_types, copy_types) if o != c)

            num_diffs += col_diffs

            if num_diffs > 1:
                mirror_impossible = True
                break

        if num_diffs == 0:
            print("Found proper mirror at row", mirror_row)
            mirror_impossible = True

        if not mirror_impossible:
            mirrors_found.append(mirror_row)

    return mirrors_found


def score(mirror: PlanarMap) -> int:
    mirror_cols = find_mirror_cols(mirror)
    mirror_rows = find_mirror_rows(mirror)

    return sum(map(math.floor, mirror_cols)) + 100 * sum(map(math.floor, mirror_rows))


def calculate_solution(input_values: InputType) -> int:
    mirror_maps = [PlanarMap(inp) for inp in input_values]

    check_sum = 0

    for mirror in mirror_maps:
        check_sum += score(mirror)

    return check_sum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
