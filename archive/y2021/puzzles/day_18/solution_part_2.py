from typing import List

from archive.y2021.puzzles.day_18.input_part_1 import SnailNumberListRep, get_input
from archive.y2021.puzzles.day_18.solution_part_1 import SnailNumber


def calculate_solution(input_values: List[SnailNumberListRep]) -> int:
    snail_numbers = [SnailNumber.from_rep(rep) for rep in input_values]
    current_max = 0

    for i in range(len(snail_numbers)):
        for j in range(len(snail_numbers)):
            if i == j:
                continue

            first = SnailNumber.from_rep(input_values[i])
            second = SnailNumber.from_rep(input_values[j])

            next_mag = (first + second).magnitude()

            if next_mag > current_max:
                current_max = next_mag

    return current_max


if __name__ == "__main__":
    print(calculate_solution(get_input()))
