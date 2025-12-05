from archive.y2024.puzzles.day_05.load_inputs import input_reader, InputType


def satisfies(sequence: list[int], rules: list[tuple[int, int]]) -> bool:
    for comes_first, comes_last in rules:
        try:
            before_index = sequence.index(comes_first)
            after_index = sequence.index(comes_last)
        except ValueError:
            pass
        else:
            if after_index <= before_index:
                return False

    return True


def calculate_solution(input_values: InputType) -> int:
    rules, sequences = input_values

    check_sum = 0

    for sequence in sequences:
        if satisfies(sequence, rules):
            check_sum += sequence[(len(sequence) - 1) // 2]

    return check_sum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
