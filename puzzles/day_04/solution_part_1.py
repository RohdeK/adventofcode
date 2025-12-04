from puzzles.day_04.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import PlanarMap


def calculate_solution(input_values: InputType) -> int:
    rolls = PlanarMap(input_values)

    accessible = 0

    for roll in rolls.iter_by_type("@"):
        surrounding = 0

        for tile in rolls.surrounding(roll):
            if tile.type == "@":
                surrounding += 1

        if surrounding < 4:
            accessible += 1

    return accessible


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
