from typing import Dict

from puzzles.day_08.load_inputs import Locator, input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    (move_pattern, ), locators = input_values
    locators_by_from: Dict[str, Locator] = {lc.from_: lc for lc in locators}

    current_locations = [lc.from_ for lc in locators if lc.from_.endswith("A")]
    current_iteration = 0

    while not all(lc.endswith("Z") for lc in current_locations):
        for i, lc in enumerate(current_locations):
            loc = locators_by_from[lc]
            direction = {"L": 0, "R": 1}[move_pattern[current_iteration % len(move_pattern)]]
            current_locations[i] = [loc.left_, loc.right_][direction]

        current_iteration += 1

    return current_iteration


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
