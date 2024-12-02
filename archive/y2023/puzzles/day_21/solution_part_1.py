from typing import Dict, List

from puzzles.day_21.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Location, PlanarMap, Position


class GardenMap(PlanarMap):
    def __init__(self, locations: List[Location]):
        super().__init__(locations)
        self.tile_min_distances: Dict[Position, int] = {}

    def double_step(self, times: int) -> int:
        self.tile_min_distances.clear()

        tiles_to_check = self.tiles_by_type["S"]

        step_num = 0
        while step_num < times:
            step_num += 1

            tiles_to_check_next_iteration = []

            for location in tiles_to_check:
                for loc in (
                    self.get_location_north(location),
                    self.get_location_east(location),
                    self.get_location_west(location),
                    self.get_location_south(location),
                ):
                    if loc is None:
                        continue

                    if loc.type == "#":
                        continue

                    if loc.position() not in self.tile_min_distances:
                        self.tile_min_distances[loc.position()] = step_num
                        tiles_to_check_next_iteration.append(loc)

            tiles_to_check = tiles_to_check_next_iteration

        return sum(1 for v in self.tile_min_distances.values() if v % 2 == 0)


def calculate_solution(input_values: InputType, num_steps: int) -> int:
    gmap = GardenMap(input_values[0])

    return gmap.double_step(num_steps)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input, 64))
