from archive.y2024.puzzles.day_18.load_inputs import input_reader, InputType
from archive.y2024.puzzles.day_18.solution_part_1 import calculate_solution as solution_part_1
from utils.common_structures.planar_map import Position


def is_blocked(input_values: InputType, numloc: int, gridsize: Position) -> bool:
    sol = solution_part_1(input_values, numloc, gridsize)
    if sol > 1000000000:
        return True
    else:
        return False


def calculate_solution(input_values: InputType, gridsize: Position) -> Position:
    vals_from, vals_to = 0, len(input_values) - 1

    while vals_from < vals_to:
        next_val = (vals_from + vals_to) // 2
        print(next_val, vals_from, vals_to)

        if is_blocked(input_values, next_val, gridsize):
            vals_to = next_val
        elif vals_from == next_val:
            vals_from += 1
        else:
            vals_from = next_val

    return tuple(input_values[vals_from - 1])


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input, (70, 70)))
