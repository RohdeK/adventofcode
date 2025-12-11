import itertools

from puzzles.day_09.load_inputs import input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    max_area = 0

    for (x0, y0), (x1, y1) in itertools.combinations(input_values, 2):
        area = (abs((x0 - x1)) + 1) * (abs((y0 - y1)) + 1)

        if area > max_area:
            max_area = area

    return max_area


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
