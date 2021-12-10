from typing import List
from puzzles.day_01.input_part_1 import get_input


def count_increases(input_list: List[int]) -> int:
    inc = 0

    prev_val = None

    for val in input_list:
        if prev_val is not None:
            if val > prev_val:
                inc += 1

        prev_val = val

    return inc


if __name__ == "__main__":
    print(count_increases(get_input()))
