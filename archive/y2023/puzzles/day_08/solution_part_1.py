from typing import Dict

from puzzles.day_08.load_inputs import Locator, input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    (move_pattern, ), locators = input_values
    locators_by_from: Dict[str, Locator] = {lc.from_: lc for lc in locators}
    current_location = "AAA"
    current_iteration = 0

    while current_location != "ZZZ":
        loc = locators_by_from[current_location]
        direction = {"L": 0, "R": 1}[move_pattern[current_iteration % len(move_pattern)]]
        current_location = [loc.left_, loc.right_][direction]
        current_iteration += 1

    return current_iteration


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
