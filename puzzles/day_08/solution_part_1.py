import itertools

from puzzles.day_08.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Located, PlanarMap


def calculate_solution(input_values: InputType) -> int:
    antennaes = PlanarMap(input_values)
    locations = set()

    for a_type in antennaes.tiles_by_type:
        if a_type == ".":
            continue

        tiles_of_type = antennaes.tiles_by_type[a_type]

        for t_1, t_2 in itertools.combinations(tiles_of_type, 2):
            diff_vec = Located(t_1.row - t_2.row, t_1.col - t_2.col)

            loc_1 = t_1.row + diff_vec.row, t_1.col + diff_vec.col
            loc_2 = t_2.row - diff_vec.row, t_2.col - diff_vec.col

            if loc_1 in antennaes.tiles_by_loc:
                locations.add(loc_1)

            if loc_2 in antennaes.tiles_by_loc:
                locations.add(loc_2)

    return len(locations)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
