from typing import Dict, List

from puzzles.day_14.load_inputs import input_reader, InputType, Position


class DrainingSandCave:
    def __init__(self):
        self.sand_influx_point = (500, 0)
        self.blocked_positions: Dict[Position, str] = {}
        self.out_of_bounds_y = 0

    def set_blocked_position(self, position: Position, solid_type="sand") -> None:
        self.blocked_positions[position] = solid_type

        if position[0] > self.out_of_bounds_y:
            self.out_of_bounds_y = position[0]

    def set_blocked_rock_path(self, path_desc: List[Position]) -> None:
        iter_start = path_desc[0]

        for iter_target in path_desc[1:]:
            x_start, x_end = sorted((iter_start[0], iter_target[0]))
            y_start, y_end = sorted((iter_start[1], iter_target[1]))

            for x in range(x_start, x_end + 1):
                for y in range(y_start, y_end + 1):
                    self.set_blocked_position((x, y), "rock")

            iter_start = iter_target

    def run_sand(self) -> bool:
        safety_iter_break = 1000
        sand_position = self.sand_influx_point

        while True:
            safety_iter_break -= 1
            new_position = self.drop_sand_once(sand_position)

            if self.is_out_of_bounds(new_position):
                return False

            if new_position == sand_position:
                self.set_blocked_position(new_position)
                return True

            sand_position = new_position

            if safety_iter_break == 0:
                raise RuntimeError(f"Sand did not converge {new_position}")

    def is_out_of_bounds(self, position: Position) -> bool:
        return position[1] > self.out_of_bounds_y

    def is_free(self, position: Position) -> bool:
        return position not in self.blocked_positions

    def drop_sand_once(self, from_position: Position) -> Position:
        candidates_in_order = [
            (from_position[0], from_position[1] + 1),
            (from_position[0] - 1, from_position[1] + 1),
            (from_position[0] + 1, from_position[1] + 1),
        ]

        for candidate in candidates_in_order:
            if self.is_free(candidate):
                return candidate

        return from_position

    def get_sand_position_count(self) -> int:
        return list(self.blocked_positions.values()).count("sand")


def calculate_solution(input_values: InputType) -> int:
    sand_grid = DrainingSandCave()

    for path in input_values:
        sand_grid.set_blocked_rock_path(path)

    while sand_grid.run_sand():
        pass

    return sand_grid.get_sand_position_count()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
