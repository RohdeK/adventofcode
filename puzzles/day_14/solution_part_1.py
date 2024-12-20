from puzzles.day_14.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Position


def get_quadrant_of(pos: Position, vec: Position, max_sides: Position, n_times: int) -> int:
    x_pos = (pos[0] + n_times * vec[0]) % max_sides[0]
    y_pos = (pos[1] + n_times * vec[1]) % max_sides[1]

    middle_x = (max_sides[0] - 1) // 2
    middle_y = (max_sides[1] - 1) // 2

    if x_pos < middle_x and y_pos < middle_y:
        return 1

    if x_pos < middle_x and y_pos > middle_y:
        return 2

    if x_pos > middle_x and y_pos < middle_y:
        return 3

    if x_pos > middle_x and y_pos > middle_y:
        return 4

    return 0


def calculate_solution(input_values: InputType, max_sides: Position) -> int:
    vals_per_quad = {}

    for p, v in input_values:
        quad = get_quadrant_of(p, v, max_sides, 100)
        vals_per_quad[quad] = vals_per_quad.get(quad, 0) + 1

    return vals_per_quad[1] * vals_per_quad[2] * vals_per_quad[3] * vals_per_quad[4]


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input, (101, 103)))
