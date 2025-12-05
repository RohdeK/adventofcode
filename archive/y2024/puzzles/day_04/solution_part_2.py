from archive.y2024.puzzles.day_04.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import PlanarMap, parse_map_lines


def calculate_solution(input_values: InputType) -> int:
    locations = parse_map_lines(input_values)
    map = PlanarMap(locations)

    xmasses = 0

    for a_tile in map.tiles_by_type["A"]:
        ne = map.get_location_northeast(a_tile)
        sw = map.get_location_southwest(a_tile)

        if ne is None or sw is None:
            continue

        diag_1 = ne.type + sw.type

        if diag_1 not in ("MS", "SM"):
            continue

        nw = map.get_location_northwest(a_tile)
        se = map.get_location_southeast(a_tile)

        if nw is None or se is None:
            continue

        diag_2 = nw.type + se.type

        if diag_2 not in ("MS", "SM"):
            continue

        xmasses += 1

    return xmasses


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
