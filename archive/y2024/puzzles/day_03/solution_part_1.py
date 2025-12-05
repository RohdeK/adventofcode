import re

from archive.y2024.puzzles.day_03.load_inputs import input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    mul_regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches = mul_regex.findall(input_values)

    checksum = 0

    for match in matches:
        checksum += int(match[0]) * int(match[1])

    return checksum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
