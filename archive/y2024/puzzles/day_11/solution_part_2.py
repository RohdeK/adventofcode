from puzzles.day_11.load_inputs import input_reader, InputType
from puzzles.day_11.solution_part_1 import blink_rule


def grouped_blink(values: dict[int, int]) -> dict[int, int]:
    new_values = {}

    for value, occurrences in values.items():
        if occurrences == 0:
            continue

        for new_value in blink_rule(value):
            new_values[new_value] = new_values.get(new_value, 0) + occurrences

    return new_values


def calculate_solution(input_values: InputType, nblinks: int) -> int:
    grouped_values = {v: input_values.count(v) for v in set(input_values)}

    for _ in range(nblinks):
        grouped_values = grouped_blink(grouped_values)

    return sum(v for v in grouped_values.values())


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input, 75))
