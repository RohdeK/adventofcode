from archive.y2023.puzzles.day_01.load_inputs import input_reader, InputType
from archive.y2023.puzzles.day_01.solution_part_1 import calculate_solution as calculate_solution_1

DIGITS = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def calculate_solution(input_values: InputType) -> int:
    corrected_lines = []

    for line in input_values:
        for spelled, number in DIGITS.items():
            line = line.replace(spelled, spelled + number + spelled)

        corrected_lines.append(line)

    return calculate_solution_1(corrected_lines)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
