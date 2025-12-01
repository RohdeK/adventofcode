import re

from puzzles.day_03.load_inputs import input_reader, InputType
from puzzles.day_03.solution_part_1 import calculate_solution as calculate_solution_1


def calculate_solution(input_values: InputType) -> int:
    checksum = 0

    for do_segment in input_values.split("do()"):
        do_segment, *some_donts = do_segment.split("don't()")
        checksum += calculate_solution_1(do_segment)

    return checksum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
