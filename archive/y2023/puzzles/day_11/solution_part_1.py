import itertools

from puzzles.day_11.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Location, PlanarMap


def expand_space(space_map: PlanarMap) -> PlanarMap:
    rows_to_expand = []
    cols_to_expand = []

    for row, tiles in space_map.tiles_by_row.items():
        if all(t.type == "." for t in tiles):
            rows_to_expand.append(row)

    for col, tiles in space_map.tiles_by_col.items():
        if all(t.type == "." for t in tiles):
            cols_to_expand.append(col)

    row_map = {
        row: row + sum(r <= row for r in rows_to_expand) for row in space_map.tiles_by_row.keys()
    }
    row_expand_map = {
        row: row + sum(r < row for r in rows_to_expand) for row in rows_to_expand
    }

    col_map = {
        col: col + sum(r <= col for r in cols_to_expand) for col in space_map.tiles_by_col.keys()
    }
    col_expand_map = {
        col: col + sum(r < col for r in cols_to_expand) for col in cols_to_expand
    }

    new_tiles = []

    for tile in space_map.tiles:
        new_tiles.append(Location(row=row_map[tile.row], col=col_map[tile.col], type=tile.type))

    for new_row_index in rows_to_expand:
        for tile in space_map.tiles_by_row[new_row_index]:
            if tile.row == 4 and tile.col == 3:
                print("Here")
            new_tiles.append(Location(row=row_expand_map[tile.row], col=col_map[tile.col], type=tile.type))

    for new_col_index in cols_to_expand:
        for tile in space_map.tiles_by_col[new_col_index]:
            if tile.row == 4 and tile.col == 3:
                print("Here")
            new_tiles.append(Location(row=row_map[tile.row], col=col_expand_map[tile.col], type=tile.type))

    for new_row_index in rows_to_expand:
        for new_col_index in cols_to_expand:
            new_tiles.append(Location(row=row_expand_map[new_row_index], col=col_expand_map[new_col_index], type="."))

    return PlanarMap(new_tiles)


def calculate_solution(input_values: InputType) -> int:
    space_map = PlanarMap(input_values[0])

    space_map = expand_space(space_map)

    galaxy_tiles = space_map.tiles_by_type["#"]

    distances = []
    g1: Location
    g2: Location
    for g1, g2 in itertools.product(galaxy_tiles, galaxy_tiles):
        vert_dist = abs(g1.row - g2.row)
        hori_dist = abs(g1.col - g2.col)

        distances.append(vert_dist + hori_dist)

    return sum(distances) // 2


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
