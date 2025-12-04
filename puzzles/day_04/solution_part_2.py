from puzzles.day_04.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import PlanarMap


def remove_if_possible(rolls: PlanarMap) -> int:
    to_remove = []

    for roll in rolls.iter_by_type("@"):
        surrounding = 0

        for tile in rolls.surrounding(roll):
            if tile.type == "@":
                surrounding += 1

        if surrounding < 4:
            to_remove.append(roll)

    for roll in to_remove:
        rolls.change_type(roll, "x")

    return len(to_remove)


def calculate_solution(input_values: InputType) -> int:
    rolls = PlanarMap(input_values)

    total_removed = 0

    iter_removed = remove_if_possible(rolls)

    while iter_removed > 0:
        total_removed += iter_removed
        iter_removed = remove_if_possible(rolls)

    return total_removed


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
