from functools import reduce
from typing import Iterator, List, Tuple

from puzzles.day_18.input_part_1 import SnailNumber, get_input


def calculate_magnitude(number: SnailNumber) -> int:
    first_part, second_part = number

    if isinstance(first_part, int):
        first_part_magnitude = first_part
    else:
        first_part_magnitude = calculate_magnitude(first_part)

    if isinstance(second_part, int):
        second_part_magnitude = second_part
    else:
        second_part_magnitude = calculate_magnitude(second_part)

    return 3 * first_part_magnitude + 2 * second_part_magnitude


def add_snail_numbers(number_1: SnailNumber, number_2: SnailNumber) -> SnailNumber:
    print("Adding", number_1, number_2)
    intermediate_number: SnailNumber = [number_1, number_2]

    return breakdown(intermediate_number)


def breakdown(number: SnailNumber) -> SnailNumber:
    while True:
        number, work_done = breakdown_explode(number)

        if work_done:
            continue

        number, work_done = breakdown_split(number)

        if work_done:
            continue

        print("Done breaking down.")

        break

    return number


def add_value_to_rightmost_in_number(number: SnailNumber, add: int) -> None:
    immediate_prev = None

    for immediate_prev, _ in walk_numerals(number):
        pass

    assert immediate_prev and isinstance(immediate_prev[1], int)

    immediate_prev[1] += add


def add_value_to_leftmost_in_number(number: SnailNumber, add: int) -> None:
    for immediate_next, _ in walk_numerals(number):
        immediate_next[0] += add
        break


def breakdown_explode(number: SnailNumber) -> Tuple[SnailNumber, bool]:
    print("Checking explode")
    found_explode_value = False
    previous_pair = None
    current_pair = None
    next_pair = None

    for iter_pair, depth in walk_numerals(number):
        if current_pair is not None:
            next_pair = iter_pair
            break

        if depth == 4:
            current_pair = iter_pair

        if not current_pair:
            previous_pair = iter_pair

    if current_pair:
        print("Exploding on", current_pair)
        found_explode_value = True
        left_val, right_val = current_pair

        if previous_pair:
            if current_pair == previous_pair[1]:
                previous_pair[1] = 0

                if isinstance(previous_pair[0], int):
                    previous_pair[0] += left_val
                else:
                    add_value_to_rightmost_in_number(previous_pair[0], left_val)
            elif next_pair == previous_pair[1]:
                previous_pair[0] += left_val
            else:
                add_value_to_rightmost_in_number(previous_pair, left_val)

        if next_pair:
            if current_pair == next_pair[0]:
                next_pair[0] = 0

                if isinstance(next_pair[1], int):
                    next_pair[1] += right_val
                else:
                    add_value_to_leftmost_in_number(next_pair[1], right_val)
            elif previous_pair == next_pair[0]:
                next_pair[1] += right_val
            else:
                add_value_to_leftmost_in_number(next_pair, right_val)

    print("Done exploding", found_explode_value)

    return number, found_explode_value


def breakdown_split(number: SnailNumber) -> Tuple[SnailNumber, bool]:
    print("Checking split")

    found_split_value = False

    for pair, _ in walk_numerals(number):
        first_part = pair[0]
        second_part = pair[1]

        if isinstance(first_part, int) and first_part > 10:
            pair[0] = pair_split(first_part)
            print("Split", first_part, pair[0])
            found_split_value = True
            break
        elif isinstance(second_part, int) and second_part > 10:
            pair[1] = pair_split(second_part)
            print("Split", second_part, pair[1])
            found_split_value = True
            break

    print("Done splitting", found_split_value)

    return number, found_split_value


def walk_numerals(number: SnailNumber, depth=0) -> Iterator[Tuple[SnailNumber, int]]:
    part_1, part_2 = number

    if isinstance(part_1, int):
        yield number, depth
    else:
        yield from walk_numerals(part_1, depth + 1)

    if isinstance(part_2, int):
        if not isinstance(part_1, int):
            yield number, depth
    else:
        yield from walk_numerals(part_2, depth + 1)


def is_atomic(number: SnailNumber) -> bool:
    return all(isinstance(val, int) for val in number)


def pair_split(value: int) -> List[int]:
    half = value // 2
    return [half, value - half]


def calculate_solution(input_values: List[SnailNumber]) -> int:
    final_number = input_values.pop(0)

    while input_values:
        final_number = add_snail_numbers(final_number, input_values.pop(0))

    return calculate_magnitude(final_number)


if __name__ == "__main__":
    print(calculate_solution(get_input()))
