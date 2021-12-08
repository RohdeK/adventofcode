from statistics import median
from typing import List

from puzzles.day_7.input_part_1 import get_input


def move_into_line(input_values: List[int]) -> int:
    optimal_position = int(median(input_values))

    return sum(abs(pos - optimal_position) for pos in input_values)


if __name__ == "__main__":
    print(move_into_line(get_input()))
