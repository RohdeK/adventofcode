from collections import deque

from puzzles.day_21.load_inputs import input_reader, InputType


def run_commands(script: str, human_input: int) -> int:
    local_dict = {"humn": human_input}

    exec(script, globals(), local_dict)

    return local_dict["root"]


def iter_find_corrective_magnitude(script: str) -> int:
    current_nearest = 1
    baseline = run_commands(script, current_nearest)
    baseline_positive = baseline > 0

    while (baseline > 0) is baseline_positive:
        current_nearest *= 10
        baseline = run_commands(script, current_nearest)

    return current_nearest // 10


def iter_nearing_on_mangniture(script: str, current_input: int, inspect_magnitude: int) -> int:
    current_result = run_commands(script, current_input)
    current_result_positive = current_result > 0

    for _ in range(1, 10):
        iter_result = run_commands(script, current_input + inspect_magnitude)

        if iter_result != 0 and (iter_result > 0) is not current_result_positive:
            break

        current_input += inspect_magnitude

    return current_input


def iter_find_zero(script: str) -> int:
    magnitude = iter_find_corrective_magnitude(script)
    result = iter_nearing_on_mangniture(script, magnitude, magnitude)

    while run_commands(script, result) != 0:
        magnitude //= 10
        result = iter_nearing_on_mangniture(script, result, magnitude)

    return result


def calculate_solution(input_values: InputType) -> int:
    input_values = [line.replace(": ", " = ") for line in input_values]
    non_evalled = deque(input_values)
    corrected_order = deque()

    while len(non_evalled):
        next_command = non_evalled.popleft()
        try:
            exec(next_command)
        except NameError:
            non_evalled.append(next_command)
        else:
            if not next_command.startswith("humn"):
                corrected_order.append(next_command)
            if next_command.startswith("root"):
                corrected_order.append(next_command.replace("+", "-"))

    script = "\n".join(corrected_order)

    return iter_find_zero(script)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
