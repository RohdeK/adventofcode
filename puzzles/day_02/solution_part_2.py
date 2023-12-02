from functools import reduce
from typing import Dict, List


from puzzles.day_02.load_inputs import input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    game_powers: List[int] = []

    for game in input_values:
        game_name, game_content = game.split(": ")
        game_steps = game_content.split("; ")

        color_counts: Dict[str, int] = {}

        for game_step in game_steps:
            color_samples = game_step.split(", ")

            for sample in color_samples:
                cube_count, color_name = sample.split(" ")

                color_counts[color_name] = max(color_counts.get(color_name, 0), int(cube_count))

        game_powers.append(reduce(lambda x, y: x * y, color_counts.values()))

    return sum(game_powers)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
