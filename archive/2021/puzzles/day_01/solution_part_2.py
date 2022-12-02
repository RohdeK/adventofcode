from typing import List
from puzzles.day_01.load_inputs import get_input
from puzzles.day_01.solution_part_1 import count_increases


def moving_sum(input_values: List[int], moving_window: int) -> List[int]:
    result_list: List[int] = []

    for i in range(len(input_values) - moving_window + 1):
        result_list.append(sum(input_values[i : i + moving_window]))

    return result_list


if __name__ == "__main__":
    print(count_increases(moving_sum(get_input(), 3)))
