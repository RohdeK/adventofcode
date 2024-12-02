import re

from puzzles.day_01.load_inputs import input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    check_sum = 0

    for line in input_values:
        only_digits = re.sub(r"\D", "", line)
        check_number = int(only_digits[0] + only_digits[-1])
        check_sum += check_number

    return check_sum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
