from functools import cmp_to_key

from archive.y2022.puzzles.day_13.load_inputs import NestedList, input_reader, InputType
from archive.y2022.puzzles.day_13.solution_part_1 import is_in_right_order


def compare(left_value: NestedList, right_value: NestedList) -> int:
    return {
        True: -1,
        False: 1,
        None: 0,
    }[is_in_right_order(left_value, right_value)]


def calculate_solution(input_values: InputType) -> int:
    input_values = [single for pair in input_values for single in pair]
    input_values.append([[2]])
    input_values.append([[6]])

    input_values.sort(key=cmp_to_key(compare))

    first_decoder_index = input_values.index([[2]]) + 1
    second_decoder_index = input_values.index([[6]]) + 1

    return first_decoder_index * second_decoder_index


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
