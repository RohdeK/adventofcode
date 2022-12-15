from typing import Dict, Set

from tqdm import tqdm

from puzzles.day_15.load_inputs import InputType, Position, input_reader


class SecondBeaconGrid:
    def __init__(self, max_coord: int):
        self.sensors_and_distances: Dict[Position, int] = {}
        self.possible_locations: Set[Position] = set()
        self.max_coord = max_coord

    @staticmethod
    def calc_distance(pos_1: Position, pos_2: Position) -> int:
        return abs(pos_1[0] - pos_2[0]) + abs(pos_1[1] - pos_2[1])

    def add_sensor(self, sensor: Position, beacon: Position) -> None:
        distance_from_sensor = self.calc_distance(sensor, beacon)

        self.sensors_and_distances[sensor] = distance_from_sensor

    def check_outlines(self) -> None:
        for sensor, distance in tqdm(self.sensors_and_distances.items()):
            self.check_sensoric_outline(sensor, distance)

    def check_sensoric_outline(self, sensor: Position, distance: int) -> None:
        for y in range(sensor[1] - distance - 1, sensor[1] + distance + 2):
            y_dist = abs(sensor[1] - y)

            x_left = sensor[0] - distance + y_dist - 1
            self.probably_add((x_left, y))

            x_right = sensor[0] + distance - y_dist + 1
            self.probably_add((x_right, y))

    def probably_add(self, position: Position) -> None:
        if position[0] < 0 or position[1] < 0:
            return
        if position[0] > self.max_coord or position[1] > self.max_coord:
            return

        for sensor, no_go_distance in self.sensors_and_distances.items():
            distance = self.calc_distance(sensor, position)

            if distance <= no_go_distance:
                return

        self.possible_locations.add(position)


def calculate_solution(input_values: InputType, max_coord: int) -> int:
    grid = SecondBeaconGrid(max_coord=max_coord)

    for sensor, beacon in input_values:
        grid.add_sensor(sensor, beacon)

    grid.check_outlines()

    final_x, final_y = grid.possible_locations.pop()

    return final_x * 4000000 + final_y


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input, 4000000))
