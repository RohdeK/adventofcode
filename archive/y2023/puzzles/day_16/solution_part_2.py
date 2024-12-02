from puzzles.day_16.load_inputs import input_reader, InputType
from puzzles.day_16.solution_part_1 import MirrorMap


def calculate_solution(input_values: InputType) -> int:
    mirrors = MirrorMap(input_values[0])

    max_location_count = 0
    best_positions = []

    positions_to_check = []

    for row in mirrors.row_indices():
        for col, direction in [(1, "west"), (max(mirrors.col_indices()), "east")]:
            positions_to_check.append((row, col, direction))

    for col in mirrors.col_indices():
        for row, direction in [(1, "north"), (max(mirrors.row_indices()), "south")]:
            positions_to_check.append((row, col, direction))

    for row, col, direction in positions_to_check:
        locations = mirrors.get_energized_locations((row, col), direction)

        if len(locations) == max_location_count:
            best_positions.append((row, col, direction))
        elif len(locations) > max_location_count:
            max_location_count = len(locations)
            best_positions = [(row, col, direction)]

    print("Best starting spots:")
    for pos in best_positions:
        print(pos)

    return max_location_count


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
