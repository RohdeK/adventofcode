from functools import reduce

from puzzles.day_16.input_part_1 import get_input
from puzzles.day_16.solution_part_1 import BITS


def evaluate(bit: BITS) -> int:
    if bit.is_literal:
        return int("".join(f"{val:04b}" for val in bit.literal_content), base=2)

    else:
        sub_values = [evaluate(sub) for sub in bit.operator_packages]

        if bit.type == 0:
            return sum(sub_values)
        elif bit.type == 1:
            return reduce(lambda x, y: x * y, sub_values)
        elif bit.type == 2:
            return min(sub_values)
        elif bit.type == 3:
            return max(sub_values)
        elif bit.type == 5:
            return int(sub_values[0] > sub_values[1])
        elif bit.type == 6:
            return int(sub_values[0] < sub_values[1])
        elif bit.type == 7:
            return int(sub_values[0] == sub_values[1])
        else:
            raise ValueError(f"Unkown type: {bit.type}.")


def calculate_solution(input_values) -> int:
    bitrep = BITS(hex_rep=input_values)

    return evaluate(bitrep)


if __name__ == "__main__":
    print(calculate_solution(get_input()))
