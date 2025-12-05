from archive.y2024.puzzles.day_15.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Direction, Location, PlanarMap


class Sokoban(PlanarMap):
    def __init__(self, locations: list[Location]):
        super().__init__(locations)

    def move(self, direc: Direction) -> None:
        mover = self.get_mover()
        tiles_to_potentially_move = []
        iter_tile = mover

        while True:
            if self.is_wall(iter_tile):
                return

            if self.is_empty(iter_tile):
                break

            tiles_to_potentially_move.append(iter_tile)
            iter_tile = self.get_location_dir(iter_tile, direc)

        while tiles_to_potentially_move:
            self.move_object(tiles_to_potentially_move.pop(-1), direc)

    @staticmethod
    def is_wall(tile: Location) -> bool:
        return tile.type == "#"

    @staticmethod
    def is_empty(tile: Location) -> bool:
        return tile.type == "."

    @staticmethod
    def is_obstacle(tile: Location) -> bool:
        return tile.type == "O"

    def get_mover(self) -> Location:
        return self.tiles_by_type["@"][0]

    def move_object(self, tile: Location, direc: Direction) -> None:
        tile_to_direc = self.get_location_dir(tile, direc)

        assert self.is_empty(tile_to_direc)
        assert not self.is_wall(tile)
        assert not self.is_empty(tile)

        self.change_type(tile_to_direc, tile.type)
        self.change_type(tile, ".")

    def gps(self) -> int:
        checksum = 0

        for tile in self.tiles_by_type["O"]:
            checksum += (tile.row - 1) * 100 + (tile.col - 1)

        return checksum


def calculate_solution(input_values: InputType) -> int:
    soko = Sokoban(input_values[0])

    for direction in input_values[1]:
        soko.move(direction)

    return soko.gps()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
