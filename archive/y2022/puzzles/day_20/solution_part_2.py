from archive.y2022.puzzles.day_20.load_inputs import input_reader, InputType
from archive.y2022.puzzles.day_20.solution_part_1 import Number, checksum, mix


def calculate_solution(input_values: InputType) -> int:
    enc_key = 811589153
    size = len(input_values) - 1
    numbers = [Number(i * enc_key, size) for i in input_values]

    for i in tuple(numbers) * 10:
        mix(i, numbers)

    return checksum(numbers)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))


