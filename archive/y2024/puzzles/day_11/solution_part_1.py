from puzzles.day_11.load_inputs import input_reader, InputType


def blink_rule(val: int) -> list[int]:
    if val == 0:
        return [1]
    elif len(str(val)) % 2 == 0:
        return [int(str(val)[:(len(str(val)) // 2)]), int(str(val)[(len(str(val)) // 2):])]
    else:
        return [val * 2024]


def blink(values: InputType) -> InputType:
    new_values = []

    for val in values:
        new_values.extend(blink_rule(val))

    return new_values


def calculate_solution(input_values: InputType, nblinks: int) -> int:
    iter_values = input_values

    for _ in range(nblinks):
        iter_values = blink(iter_values)

    return len(iter_values)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input, 25))
