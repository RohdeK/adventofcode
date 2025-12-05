from puzzles.day_05.load_inputs import input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    ranges, ings = input_values

    fresh = 0

    for ing in ings:
        if any(ing in rng for rng in ranges):
            fresh += 1

    return fresh


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
