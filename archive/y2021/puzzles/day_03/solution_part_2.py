from collections import Counter
from typing import List

from archive.y2021.puzzles.day_03.input_part_1 import get_input
from archive.y2021.puzzles.day_03.solution_part_1 import transpose_values


def calculate_oxygen_rate(input_values: List[str]) -> int:
    assumed_digit_length = len(input_values[0])

    oxygen_rate_binary = None

    for i in range(assumed_digit_length):
        transposed_values = transpose_values(input_values)

        counter = Counter(transposed_values[i]).most_common(2)

        if counter[0][1] == counter[1][1]:
            criterium = "1"
        else:
            criterium = counter[0][0]

        reduced_values = [value for value in input_values if value[i] == criterium]

        if len(reduced_values) == 1:
            oxygen_rate_binary = reduced_values[0]
            break
        elif len(reduced_values) == 0:
            oxygen_rate_binary = input_values[-1]
            break
        else:
            input_values = reduced_values

    oxygen_rate = int("".join(oxygen_rate_binary), base=2)

    return oxygen_rate


def calculate_co2_rate(input_values: List[str]) -> int:
    assumed_digit_length = len(input_values[0])

    co2_rate_binary = None

    for i in range(assumed_digit_length):
        transposed_values = transpose_values(input_values)

        counter = Counter(transposed_values[i]).most_common(2)

        if counter[0][1] == counter[1][1]:
            criterium = "0"
        else:
            criterium = counter[1][0]

        reduced_values = [value for value in input_values if value[i] == criterium]

        if len(reduced_values) == 1:
            co2_rate_binary = reduced_values[0]
            break
        elif len(reduced_values) == 0:
            co2_rate_binary = input_values[-1]
            break
        else:
            input_values = reduced_values

    co2rate = int("".join(co2_rate_binary), base=2)

    return co2rate


if __name__ == "__main__":
    oxy_rate = calculate_oxygen_rate(get_input())
    co2_rate = calculate_co2_rate(get_input())

    print(oxy_rate * co2_rate)
