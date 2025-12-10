import itertools

from puzzles.day_10.load_inputs import Machine, input_reader, InputType


def solve_machine(m: Machine) -> int:
    min_activations = len(m.buttons)

    for btn_active in itertools.product(*[[True, False]]*len(m.buttons)):
        activations = sum(btn_active)

        if activations >= min_activations:
            continue

        target = m.target_state.copy()

        for activation, button in zip(btn_active, m.buttons):
            if activation:
                for idx in button:
                    target[idx] = not target[idx]

        if not any(target):
            min_activations = activations

    return min_activations


def calculate_solution(input_values: InputType) -> int:
    checksum = 0

    for machine in input_values:
        checksum += solve_machine(machine)

    return checksum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
