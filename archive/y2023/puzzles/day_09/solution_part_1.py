from typing import List

from puzzles.day_09.load_inputs import input_reader, InputType


def solve_hist(hist: List[int]) -> int:
    last_values = []
    iter_hist = hist

    while any(x != 0 for x in iter_hist):
        last_values.append(iter_hist[-1])
        iter_hist = [iter_hist[i] - iter_hist[i - 1] for i in range(1, len(iter_hist))]

    return sum(last_values)


def calculate_solution(input_values: InputType) -> int:
    checksum = 0

    for hist in input_values:
        checksum += solve_hist(hist)

    return checksum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
