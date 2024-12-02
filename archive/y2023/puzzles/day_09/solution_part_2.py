from typing import List

from puzzles.day_09.load_inputs import input_reader, InputType


def alternating_sum(values: List[int]) -> int:
    result = 0
    alt_mode = False
    for v in values:
        result += (-v if alt_mode else v)
        alt_mode = not alt_mode

    return result


def solve_hist(hist: List[int]) -> int:
    fist_values = []
    iter_hist = hist

    while any(x != 0 for x in iter_hist):
        fist_values.append(iter_hist[0])
        iter_hist = [iter_hist[i] - iter_hist[i - 1] for i in range(1, len(iter_hist))]

    return alternating_sum(fist_values)


def calculate_solution(input_values: InputType) -> int:
    checksum = 0

    for hist in input_values:
        checksum += solve_hist(hist)

    return checksum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
