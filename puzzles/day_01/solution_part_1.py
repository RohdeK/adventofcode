from typing import List

from puzzles.day_01.input_part_1 import get_input


def calculate_solution(input_values: List[List[int]]) -> int:
    calory_sum = [
        sum(per_elf) for per_elf in input_values
    ]

    return max(calory_sum)


if __name__ == "__main__":
    print(calculate_solution(get_input()))
