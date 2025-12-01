from collections import defaultdict

from puzzles.day_12.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Location, PlanarMap


class GardenMap(PlanarMap):
    def detect_regions(self) -> list[list[Location]]:
        handled_tiles = []
        regions = []

        for planttype in self.tiles_by_type:
            for starting_tile in self.tiles_by_type[planttype]:
                if starting_tile in handled_tiles:
                    continue

                tile_region = self.detect_region_of(starting_tile)

                regions.append(tile_region)
                handled_tiles.extend(tile_region)

        return regions

    def detect_region_of(self, tile: Location) -> list[Location]:
        tiles_of_region = []
        tiles_to_check = [tile]

        while tiles_to_check:
            iter_tile = tiles_to_check.pop(0)
            tiles_of_region.append(iter_tile)

            for next_tile in self.surrounding(iter_tile, False):
                if next_tile.type == tile.type:
                    if next_tile not in tiles_of_region and next_tile not in tiles_to_check:
                        tiles_to_check.append(next_tile)

        return tiles_of_region

    @staticmethod
    def calculate_fence_price(region: list[Location]) -> int:
        area = len(region)

        fence_locations = defaultdict(int)

        for loc in region:
            fence_locations[(loc.row + 0.5, loc.col)] += 1
            fence_locations[(loc.row, loc.col + 0.5)] += 1
            fence_locations[(loc.row - 0.5, loc.col)] += 1
            fence_locations[(loc.row, loc.col - 0.5)] += 1

        perimeter = sum([v == 1 for v in fence_locations.values()])

        return area * perimeter


def calculate_solution(input_values: InputType) -> int:
    garden = GardenMap(input_values)

    areas = garden.detect_regions()

    checksum = 0

    for area in areas:
        checksum += garden.calculate_fence_price(area)

    return checksum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
