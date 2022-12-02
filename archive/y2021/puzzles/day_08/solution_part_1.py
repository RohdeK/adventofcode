from typing import List

from archive.y2021.puzzles.day_08.input_part_1 import get_input


def count_unique_type_digits(input_values: List[str]) -> int:
    unique_count = 0

    for signals in input_values:
        _, output_part = signals.split("|")
        digit_representations = output_part.split()

        unique_count += sum([len(digit) in (2, 3, 4, 7) for digit in digit_representations])

    return unique_count


if __name__ == "__main__":
    print(count_unique_type_digits(get_input()))
