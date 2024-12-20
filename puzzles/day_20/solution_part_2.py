from typing import Iterator

from puzzles.day_20.load_inputs import input_reader, InputType
from utils.common_structures.distance_map import DistanceMap
from utils.common_structures.planar_map import Direction, Location, Position


class RaceConditionMapV2(DistanceMap):
    def __init__(self, locations: list[Location]):
        super().__init__(locations)
        self.set_starting_type("S")
        self.set_ending_type("E")
        self.update_type_weight("#", 10000)

    def possible_next_tiles(self, tile: Location) -> Iterator[tuple[Location, int]]:
        max_distance = 20

        for row_mod in range(-max_distance, max_distance + 1):
            for col_mod in range(-(max_distance - abs(row_mod)), (max_distance - abs(row_mod)) + 1):

                next_tile = self.get_location(tile.row + row_mod, tile.col + col_mod)

                if next_tile is None:
                    continue

                if next_tile.type == "#":
                    continue

                yield next_tile, abs(row_mod) + abs(col_mod)

    def find_shortcuts(self, minimum_time_save: int) -> dict[tuple[Position, Position], float]:
        skips_found = 0
        time_saves = {}

        self.measure_distances()

        for tile in self.tiles:
            if tile.type == "#":
                continue

            for next_next_tile, steps in self.possible_next_tiles(tile):
                print(steps)
                if (tile.position(), next_next_tile.position()) in time_saves:
                    print("Skipping for efficiency.")

                print(f"Checking {tile} to {next_next_tile}.")
                tile_distance = self._node_distances[tile.position()]
                skipped_distance = self._node_distances[next_next_tile.position()]
                skip_saved = skipped_distance - tile_distance - steps

                if skip_saved >= minimum_time_save:
                    print(f"Found a skip, saving {skip_saved}")
                    skips_found += 1
                    time_saves[(tile.position(), next_next_tile.position())] = skip_saved

        print(f"Found {skips_found} skips ({len(time_saves)} unique).")
        return time_saves


def calculate_solution(input_values: InputType, time_saved: int) -> int:
    race_map = RaceConditionMapV2(input_values)

    shortcuts = race_map.find_shortcuts(time_saved)

    return sum(v >= time_saved for v in shortcuts.values())


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input, 100))
