from typing import List

from puzzles.day_02.load_inputs import input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    color_counts = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    valid_ids: List[int] = []

    for game in input_values:
        game_name, game_content = game.split(": ")
        game_steps = game_content.split("; ")
        game_id = int(game_name[4:])

        game_invalid = False

        for game_step in game_steps:
            color_samples = game_step.split(", ")

            for sample in color_samples:
                cube_count, color_name = sample.split(" ")

                if int(cube_count) > color_counts[color_name]:
                    game_invalid = True

        if not game_invalid:
            valid_ids.append(game_id)

    return sum(valid_ids)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
