from archive.y2023.puzzles.day_04.load_inputs import input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    points = 0

    for winning_nums, elf_nums in input_values:
        matches = [n for n in elf_nums if n in winning_nums]

        if len(matches) > 0:
            points += 2 ** (len(matches) - 1)

    return points


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
