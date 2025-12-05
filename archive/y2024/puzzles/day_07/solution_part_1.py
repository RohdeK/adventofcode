from archive.y2024.puzzles.day_07.load_inputs import input_reader, InputType


def can_be_calculated(target_value: int, components: list[int]) -> bool:
    if len(components) == 1:
        return target_value == components[0]

    last_value = components[-1]
    pre_components = components[:-1]

    if target_value % last_value == 0:
        if can_be_calculated(target_value // last_value, pre_components):
            return True

    return can_be_calculated(target_value - last_value, pre_components)


def calculate_solution(input_values: InputType) -> int:
    check_sum = 0

    for target_value, components in input_values:
        if can_be_calculated(target_value, components):
            check_sum += target_value

    return check_sum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
