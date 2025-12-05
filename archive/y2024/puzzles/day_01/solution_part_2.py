from collections import Counter

from archive.y2024.puzzles.day_01.load_inputs import input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    list_1 = sorted([tup[0] for tup in input_values])
    list_2 = sorted([tup[1] for tup in input_values])

    value_counts_1 = Counter(list_1)
    value_counts_2 = Counter(list_2)

    check_sum = 0

    for num, cnt in value_counts_1.items():
        match_cnt = value_counts_2[num]
        check_sum += cnt * num * match_cnt

    return check_sum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
