from typing import Set

from puzzles.day_15.load_inputs import Position, input_reader, InputType


class BeaconGrid:
    def __init__(self, focus_row: int):
        self.focus_row = focus_row
        self.sensor_positions: Set[Position] = set()
        self.beacon_positions: Set[Position] = set()
        self.non_sensor_positions: Set[Position] = set()

    def add_sensor(self, sensor: Position, beacon: Position) -> None:
        self.sensor_positions.add(sensor)
        self.beacon_positions.add(beacon)
        self.on_sensor_added(sensor, beacon)

    def on_sensor_added(self, sensor: Position, beacon: Position) -> None:
        self.add_non_beacon_postitions(sensor, beacon)

    def add_non_beacon_postitions(self, sensor: Position, beacon: Position) -> None:
        distance_from_sensor = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

        if sensor in self.non_sensor_positions:
            self.non_sensor_positions.remove(sensor)

        for y in range(sensor[1] - distance_from_sensor, sensor[1] + distance_from_sensor + 1):
            if y != self.focus_row:
                continue

            y_dist = abs(sensor[1] - y)

            for x in range(sensor[0] - distance_from_sensor, sensor[0] + distance_from_sensor + 1):
                x_dist = abs(sensor[0] - x)

                if x_dist + y_dist > distance_from_sensor:
                    continue

                if (x, y) == beacon:
                    continue

                if (x, y) in self.sensor_positions:
                    continue

                self.non_sensor_positions.add((x, y))

    def count_non_positions_in_row(self) -> int:
        return len(self.non_sensor_positions)


def calculate_solution(input_values: InputType, row_nr: int) -> int:
    grid = BeaconGrid(focus_row=row_nr)

    for sensor, beacon in input_values:
        grid.add_sensor(sensor, beacon)

    return grid.count_non_positions_in_row()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input, 2000000))
