from puzzles.day_14.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Location, PlanarMap


class BoulderMap(PlanarMap):
    def roll_north(self) -> None:
        for i in sorted(self.tiles_by_row.keys()):
            for tile in self.tiles_by_row[i]:
                if tile.type == "O":
                    self.push_tile_north(tile)

    def push_tile_north(self, tile: Location) -> None:
        iter_tile = tile
        still_checking = True

        while still_checking:
            northern_tile = self.get_location_north(iter_tile)

            if northern_tile and northern_tile.type == ".":
                iter_tile = northern_tile
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

    bmap.roll_north()

    return bmap.sum_weights()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
