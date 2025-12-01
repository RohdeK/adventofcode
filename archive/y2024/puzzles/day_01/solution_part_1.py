from puzzles.day_01.load_inputs import input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    list_1 = sorted([tup[0] for tup in input_values])
    list_2 = sorted([tup[1] for tup in input_values])

    diffs = [abs(l1 - l2) for l1, l2 in zip(list_1, list_2)]

    return sum(diffs)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
