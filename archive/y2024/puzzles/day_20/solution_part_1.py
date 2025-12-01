from puzzles.day_20.load_inputs import input_reader, InputType
from utils.common_structures.distance_map import DistanceMap
from utils.common_structures.planar_map import Direction, Location, Position


class RaceConditionMap(DistanceMap):
    def __init__(self, locations: list[Location]):
        super().__init__(locations)
        self.set_starting_type("S")
        self.set_ending_type("E")
        self.update_type_weight("#", 10000)

    def find_shortcuts(self) -> dict[tuple[Position, Position], float]:
        skips_found = 0
        time_saves = {}

        self.measure_distances()

        for tile in self.tiles:
            if tile.type == "#":
                continue

            for direc in Direction:
                next_tile = self.get_location_dir(tile, direc)

                if next_tile.type != "#":
                    continue

                for next_direct in Direction:
                    next_next_tile = self.get_location_dir(next_tile, next_direct)

                    if next_next_tile is None:
                        continue

                    if next_next_tile.type == "#":
                        continue

                    print(f"Checking {tile} to {next_next_tile}.")
                    tile_distance = self._node_distances[tile.position()]
                    skipped_distance = self._node_distances[next_next_tile.position()]

                    skip_saved = skipped_distance - tile_distance - 2

                    if skip_saved > 0:
                        print(f"Found a skip, saving {skip_saved}")
                        skips_found += 1
                        time_saves[(tile.position(), next_next_tile.position())] = skip_saved

        print(f"Found {skips_found} skips ({len(time_saves)} unique).")
        return time_saves


def calculate_solution(input_values: InputType, time_saved: int) -> int:
    race_map = RaceConditionMap(input_values)

    shortcuts = race_map.find_shortcuts()

    return sum(v >= time_saved for v in shortcuts.values())


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input, 100))
