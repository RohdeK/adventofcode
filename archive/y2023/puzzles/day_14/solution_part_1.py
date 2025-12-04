from typing import Iterator

from archive.y2023.puzzles.day_14.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Location, PlanarMap


class BoulderMap(PlanarMap):
    def roll(self, direction: str) -> None:
        for tile in self.iter_optimal_direction(direction):
            if tile.type == "O":
                self.push_tile(tile, direction)

    def iter_optimal_direction(self, direction: str) -> Iterator[Location]:
        if direction == "north":
            for i in sorted(self.tiles_by_row.keys()):
                yield from self.tiles_by_row[i]
        elif direction == "south":
            for i in sorted(self.tiles_by_row.keys(), reverse=True):
                yield from self.tiles_by_row[i]
        elif direction == "west":
            for i in sorted(self.tiles_by_col.keys()):
                yield from self.tiles_by_col[i]
        elif direction == "east":
            for i in sorted(self.tiles_by_col.keys(), reverse=True):
                yield from self.tiles_by_col[i]

    def push_tile(self, tile: Location, direction: str) -> None:
        iter_tile = tile
        still_checking = True

        while still_checking:
            next_tile = self.get_location_to(iter_tile, direction)

            if next_tile and next_tile.type == ".":
                iter_tile = next_tile
            else:
                still_checking = False

        if iter_tile != tile:
            self.swap_locations(iter_tile, tile)

    def swap_locations(self, tile_1: Location, tile_2: Location) -> None:
        self.tiles_by_type[tile_1.type].remove(tile_1)
        self.tiles_by_type[tile_2.type].remove(tile_2)

        tile_1.type, tile_2.type = tile_2.type, tile_1.type

        self.tiles_by_type[tile_1.type].append(tile_1)
        self.tiles_by_type[tile_2.type].append(tile_2)

    def sum_weights(self) -> int:
        check_sum = 0
        max_row = max(self.tiles_by_row.keys())
        for tile in self.tiles_by_type["O"]:
            check_sum += max_row + 1 - tile.row
        return check_sum


def calculate_solution(input_values: InputType) -> int:
    bmap = BoulderMap(input_values[0])

    bmap.roll("north")

    return bmap.sum_weights()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
