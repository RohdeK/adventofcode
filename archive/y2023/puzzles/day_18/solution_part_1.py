from typing import List

from archive.y2023.puzzles.day_10.solution_part_2 import iter_cover_outers
from archive.y2023.puzzles.day_18.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Location, PlanarMap, Position


def normalize_locations(locations: List[Location]) -> List[Location]:
    min_row = min(loc.row for loc in locations)
    min_col = min(loc.col for loc in locations)

    for loc in locations:
        loc.row += 1 - min_row
        loc.col += 1 - min_col

    return locations


def fill_locations(locations: List[Location]) -> List[Location]:
    locations_by_loc = {(loc.row, loc.col): loc for loc in locations}

    min_row = min(loc.row for loc in locations)
    min_col = min(loc.col for loc in locations)
    max_row = max(loc.row for loc in locations)
    max_col = max(loc.col for loc in locations)

    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if (row, col) not in locations_by_loc:
                locations.append(Location(row=row, col=col, type="."))

    locations = sorted(locations, key=lambda x: x.position())

    return locations


def build_locations_from_instructions(input_values: InputType) -> List[Location]:
    locations_for_paint = []
    cl = (0, 0)
    for direction, distance, color in input_values:
        for i in range(int(distance)):
            ttype = "#"
            if direction == "D":
                cl = cl[0] + 1, cl[1]
                ttype = "v"
            elif direction == "U":
                cl = cl[0] - 1, cl[1]
                ttype = "^"
            elif direction == "L":
                cl = cl[0], cl[1] - 1
                ttype = "<"
            elif direction == "R":
                cl = cl[0], cl[1] + 1
                ttype = ">"

            locations_for_paint.append(Location(row=cl[0], col=cl[1], type=ttype))

    locations = normalize_locations(locations_for_paint)
    locations = fill_locations(locations)

    return locations


def calculate_solution(input_values: InputType) -> int:
    locations = build_locations_from_instructions(input_values)

    trench_map = PlanarMap(locations)

    # Using old solver
    iter_cover_outers(trench_map)

    print(trench_map)

    return sum(t.type != "O" for t in trench_map.tiles)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
