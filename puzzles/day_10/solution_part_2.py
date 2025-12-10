from scipy.optimize import linprog

from puzzles.day_10.load_inputs import Machine, input_reader, InputType


def solve_machine(m: Machine) -> int:
    a = []

    for i, _ in enumerate(m.joltages):
        jolt_a = []

        for but_idx, but_targets in enumerate(m.buttons):
            if i in but_targets:
                jolt_a.append(1)
            else:
                jolt_a.append(0)

        a.append(jolt_a)

    b = m.joltages
    y = [1] * len(m.buttons)
    x = linprog(y, A_eq=a, b_eq=b, integrality=1)

    return round(x.fun)


def calculate_solution(input_values: InputType) -> int:
    checksum = 0

    for machine in input_values:
        checksum += solve_machine(machine)

    return checksum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
