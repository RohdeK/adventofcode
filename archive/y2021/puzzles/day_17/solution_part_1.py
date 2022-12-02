from typing import Tuple

from archive.y2021.puzzles.day_17.input_part_1 import get_input


def calculate_solution(_hor: Tuple[int, int], vert: Tuple[int, int]) -> int:
    return abs(vert[0]) * (abs(vert[0]) - 1) // 2


if __name__ == "__main__":
    print(calculate_solution(*get_input()))
