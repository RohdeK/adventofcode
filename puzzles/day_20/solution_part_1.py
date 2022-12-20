from typing import List

from puzzles.day_20.load_inputs import input_reader, InputType


class Number:
    def __init__(self, value: int, sized: int):
        self.value = value
        if value >= 0:
            self.normalized = value % sized
        else:
            self.normalized = value % sized - sized

    def __repr__(self):
        return str(self.value)


def mix(i: Number, numbers: List[Number]):
    prev_index = numbers.index(i)
    total_shift = prev_index + i.normalized
    runs_around = total_shift // (len(numbers) - 1)

    if runs_around > 0:
        total_shift -= runs_around * (len(numbers) - 1)
        target_index = total_shift % len(numbers)
    elif runs_around < 0:
        total_shift -= (runs_around + 1) * (len(numbers) - 1)
        target_index = total_shift + len(numbers) - 1
    elif total_shift == 0 and i.normalized < 0:
        target_index = len(numbers) - 1
    else:
        target_index = total_shift

    numbers.remove(i)
    numbers.insert(target_index, i)


def checksum(numbers: List[Number]) -> int:
    zero = next(n for n in numbers if n.value == 0)
    zero_index = numbers.index(zero)
    check_positions = [1000, 2000, 3000]

    return sum(
        numbers[(pos + zero_index) % len(numbers)].value for pos in check_positions
    )


def calculate_solution(input_values: InputType) -> int:
    size = len(input_values) - 1
    numbers = [Number(i, size) for i in input_values]

    for i in tuple(numbers):
        mix(i, numbers)

    return checksum(numbers)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
