import numpy as np

from archive.y2024.puzzles.day_13.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Position


def fastest_route_cost(button_a: Position, button_b: Position, prize_loc: Position) -> int:
    eqs = np.array([(button_a[0], button_b[0]), (button_a[1], button_b[1])])
    trgs = np.array(prize_loc)
    sol = np.linalg.solve(eqs, trgs)

    if not np.isclose(sol[0] - np.round(sol[0]), 0, atol=0.001) or not np.isclose(sol[1] - np.round(sol[1]), 0, atol=0.001):
        print("Unsolvable:", sol[0] - np.round(sol[0]), sol[1] - np.round(sol[1]))
        return 0

    print(sol)

    return int(np.round(sol[0])) * 3 + int(np.round(sol[1]))


def calculate_solution(input_values: InputType) -> int:
    checksum = 0

    for setup in input_values:
        checksum += fastest_route_cost(*setup)

    return checksum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
