from typing import Optional

from puzzles.day_13.load_inputs import NestedList, input_reader, InputType


def is_in_right_order(left_value: NestedList, right_value: NestedList) -> Optional[bool]:
    if isinstance(left_value, int) and isinstance(right_value, int):
        if left_value == right_value:
            return None
        else:
            return left_value < right_value

    if isinstance(left_value, list) and isinstance(right_value, list):
        for index in range(len(left_value)):
            left_sub_value = left_value[index]
            try:
                right_sub_value = right_value[index]
            except IndexError:
                return False

            sub_decision = is_in_right_order(left_sub_value, right_sub_value)

            if sub_decision is None:
                continue
            else:
                return sub_decision

        if len(left_value) < len(right_value):
            return True
        else:
            return None

    if isinstance(left_value, int):
        left_value = [left_value]

    if isinstance(right_value, int):
        right_value = [right_value]

    return is_in_right_order(left_value, right_value)


def calculate_solution(input_values: InputType) -> int:
    index_sums = 0

    for index, pair in enumerate(input_values):
        if is_in_right_order(*pair):
            index_sums += index + 1

    return index_sums


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
