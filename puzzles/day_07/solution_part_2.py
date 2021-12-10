from statistics import mean
from typing import List

from puzzles.day_07.input_part_1 import get_input


def calculate_fuel(optimal_position: int, input_values: List[int]):
    distances = [abs(pos - optimal_position) for pos in input_values]

    return sum([dist * (dist + 1) // 2 for dist in distances])


def jitter_minimize_fuel(input_values: List[int]):
    supposed_opt = round(mean(input_values))

    init = calculate_fuel(supposed_opt, get_input())

    while True:
        one_to_right = calculate_fuel(supposed_opt + 1, input_values)
        one_to_left = calculate_fuel(supposed_opt - 1, input_values)

        if one_to_right <= init:
            init = one_to_right
            supposed_opt += 1

        elif one_to_left <= init:
            init = one_to_left
            supposed_opt -= 1

        else:
            break

    return init


if __name__ == "__main__":
    print(jitter_minimize_fuel(get_input()))
