from puzzles.day_02.load_inputs import input_reader, InputType


def is_safe(report: list[int]) -> bool:
    down_allowed_diff = (1, 2, 3)
    up_allowed_diff = (-1, -2, -3)

    diffs = [x0 - x1 for x0, x1 in zip(report[1:], report[:-1])]

    if all(d in down_allowed_diff for d in diffs):
        return True

    elif all(d in up_allowed_diff for d in diffs):
        return True

    else:
        return False


def calculate_solution(input_values: InputType) -> int:
    safe_reps = 0

    for report in input_values:
        if is_safe(report):
            safe_reps += 1

    return safe_reps


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
