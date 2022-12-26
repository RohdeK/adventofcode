import numpy as np

from puzzles.day_25.load_inputs import input_reader, InputType


def from_snafu(snafu: str) -> int:
    plus_part = snafu.replace("-", "0").replace("=", "0")
    minus_part = snafu.replace("1", "0").replace("2", "0").replace("-", "1").replace("=", "2")

    return int(plus_part, 5) - int(minus_part, 5)


def to_snafu(dec: int) -> str:
    five_rep = np.base_repr(dec, 5)
    for i in range(1, len(five_rep) + 1):
        if five_rep[-i] == "3":
            five_rep = five_rep[:-i-1] + str(int(five_rep[-i-1]) + 1) + "=" + five_rep[-i+1:]
        elif five_rep[-i] == "4":
            five_rep = five_rep[:-i-1] + str(int(five_rep[-i-1]) + 1) + "-" + five_rep[-i+1:]
        elif five_rep[-i] == "5":
            five_rep = five_rep[:-i-1] + str(int(five_rep[-i-1]) + 1) + "0" + five_rep[-i+1:]

    return five_rep


def calculate_solution(input_values: InputType) -> int:
    check_sum = 0

    for snafu in input_values:
        check_sum += from_snafu(snafu)

    return to_snafu(check_sum)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
