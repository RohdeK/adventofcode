from typing import List, Tuple
from collections import Counter

from puzzles.day_03.input_part_1 import get_input


def transpose_values(input_values: List[str]) -> List[List[str]]:
    assumed_digit_length = len(input_values[0])

    transposed_values = [[input_values[i][j] for i in range(len(input_values))] for j in range(assumed_digit_length)]

    return transposed_values


def calculate_rates(input_values: List[str]) -> Tuple[int, int]:
    transposed_values = transpose_values(input_values)

    most_common = [Counter(digits).most_common(1)[0][0] for digits in transposed_values]

    gamma_rate = int("".join(most_common), base=2)

    epsilon_rate = 2 ** len(transposed_values) - gamma_rate - 1

    return gamma_rate, epsilon_rate


if __name__ == "__main__":
    gamma, epsilon = calculate_rates(get_input())

    print(gamma * epsilon)
