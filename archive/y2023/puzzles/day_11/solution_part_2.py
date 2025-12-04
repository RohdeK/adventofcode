import itertools
from typing import List, Tuple

from archive.y2023.puzzles.day_11.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Location, PlanarMap


def theoretically_expand_space(space_map: PlanarMap) -> Tuple[List[int], List[int]]:
    rows_to_expand = []
    cols_to_expand = []

    for row, tiles in space_map.tiles_by_row.items():
        if all(t.type == "." for t in tiles):
            rows_to_expand.append(row)

    for col, tiles in space_map.tiles_by_col.items():
        if all(t.type == "." for t in tiles):
            cols_to_expand.append(col)

    return rows_to_expand, cols_to_expand


def calculate_solution(input_values: InputType, expansion_size: int) -> int:
    space_map = PlanarMap(input_values[0])

    empty_rows, empty_cols = theoretically_expand_space(space_map)

    galaxy_tiles = space_map.tiles_by_type["#"]

    distances = []
    g1: Location
    g2: Location
    for g1, g2 in itertools.product(galaxy_tiles, galaxy_tiles):
        low_row, hi_row = sorted((g1.row, g2.row))
        low_col, hi_col = sorted((g1.col, g2.col))
        vert_dist = hi_row - low_row
        hori_dist = hi_col - low_col

        for row in empty_rows:
            if low_row < row < hi_row:
                vert_dist += expansion_size

        for col in empty_cols:
            if low_col < col < hi_col:
                hori_dist += expansion_size

        if g1.position() == (1, 4) and g2.position() == (2, 8):
            print("pause")

        distances.append(vert_dist + hori_dist)

    return sum(distances) // 2


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input, 1_000_000 - 1))
