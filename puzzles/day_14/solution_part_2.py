from puzzles.day_14.load_inputs import Position, input_reader, InputType
from puzzles.day_14.solution_part_1 import DrainingSandCave


class FlooredDrainingSandCave(DrainingSandCave):
    def __init__(self):
        super().__init__()
        self.floor_level = 0

    def add_floor(self) -> None:
        max_y = max(pos[1] for pos, type_str in self.blocked_positions.items() if type_str == "rock")
        self.floor_level = max_y + 2

    def is_out_of_bounds(self, position: Position) -> bool:
        return position == self.sand_influx_point

    def is_free(self, position: Position) -> bool:
        if position[1] == self.floor_level:
            return False
        else:
            return position not in self.blocked_positions


def calculate_solution(input_values: InputType) -> int:
    sand_grid = FlooredDrainingSandCave()

    for path in input_values:
        sand_grid.set_blocked_rock_path(path)

    sand_grid.add_floor()

    while sand_grid.run_sand():
        pass

    return sand_grid.get_sand_position_count() + 1


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
