from archive.y2024.puzzles.day_05.load_inputs import input_reader, InputType
from archive.y2024.puzzles.day_05.solution_part_1 import satisfies


def fix(sequence: list[int], rules: list[tuple[int, int]]) -> list[int]:
    max_iterations = 1000

    while not satisfies(sequence, rules):
        max_iterations -= 1
        if max_iterations == 0:
            raise RuntimeError("Something is wrong.")

        print("Old sequence: ", sequence)

        for comes_first, comes_last in rules:
            try:
                before_index = sequence.index(comes_first)
                after_index = sequence.index(comes_last)
            except ValueError:
                pass
            else:
                if after_index <= before_index:
                    sequence[after_index], sequence[before_index] = sequence[before_index], sequence[after_index]
                    print("New sequence: ", sequence)
                    break

    print("Satifies: ", sequence)

    return sequence


def calculate_solution(input_values: InputType) -> int:
    rules, sequences = input_values

    check_sum = 0

    for sequence in sequences:
        if not satisfies(sequence, rules):
            fixed_sequence = fix(sequence, rules)
            check_sum += fixed_sequence[(len(fixed_sequence) - 1) // 2]

    return check_sum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
