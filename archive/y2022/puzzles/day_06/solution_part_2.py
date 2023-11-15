
from archive.y2022.puzzles.day_06.load_inputs import input_reader, InputType
from archive.y2022.puzzles.day_06.solution_part_1 import get_mark


def calculate_solution(input_values: InputType) -> int:
    return get_mark(input_values, 14)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
