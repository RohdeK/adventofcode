from archive.y2024.puzzles.day_10.load_inputs import input_reader, InputType
from archive.y2024.puzzles.day_10.solution_part_1 import TrailMap


def calculate_solution(input_values: InputType) -> int:
    trails = TrailMap(input_values)

    checksum = 0

    for thead in trails.heads():
        checksum += trails.score(thead)[1]

    return checksum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
