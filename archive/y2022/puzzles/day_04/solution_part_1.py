from archive.y2022.puzzles.day_04.load_inputs import input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    overlap_score = 0

    for first_elf, second_elf in input_values:
        first_start, first_end = first_elf
        second_start, second_end = second_elf

        if first_start >= second_start and first_end <= second_end:
            overlap_score += 1
        elif second_start >= first_start and second_end <= first_end:
            overlap_score += 1

    return overlap_score


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
