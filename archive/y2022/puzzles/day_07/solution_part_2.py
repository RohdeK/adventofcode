
from archive.y2022.puzzles.day_07.load_inputs import input_reader, InputType
from archive.y2022.puzzles.day_07.solution_part_1 import commands_parser, list_directories_with_size


def calculate_solution(input_values: InputType) -> int:
    files = commands_parser(input_values)
    dirs = list_directories_with_size(files)

    total_size = dirs["/"]
    free_space = 70000000 - total_size
    needed_space = 30000000 - free_space

    current_candidate = 70000000

    for val in dirs.values():
        if current_candidate > val >= needed_space:
            current_candidate = val

    return current_candidate


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
