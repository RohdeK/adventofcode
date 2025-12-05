from archive.y2024.puzzles.day_15.load_inputs import input_reader, InputType
from archive.y2024.puzzles.day_15.solution_part_1 import Sokoban
from utils.common_structures.planar_map import Direction, Location, parse_map_lines


class WideSokoban(Sokoban):
    def __init__(self, locations: list[Location]):
        super().__init__(self.widen(locations))

    @staticmethod
    def widen(locations: list[Location]) -> list[Location]:
        unwrapped = repr(Sokoban(locations))
        unwrapped = unwrapped.replace("#", "##")
        unwrapped = unwrapped.replace(".", "..")
        unwrapped = unwrapped.replace("O", "[]")
        unwrapped = unwrapped.replace("@", "@.")

        return parse_map_lines(unwrapped)

    def move(self, direc: Direction) -> None:
        if direc in (Direction.LEFT, Direction.RIGHT):
            super().move(direc)
            return

        mover = self.get_mover()
        tiles_to_check = [mover]
        tiles_checked = []
        tiles_to_potentially_move = []

        while tiles_to_check:
            iter_tile = tiles_to_check.pop(0)
            tiles_checked.append(iter_tile)

            if self.is_wall(iter_tile):
                return

            if self.is_empty(iter_tile):
                continue

            if iter_tile not in tiles_to_potentially_move:
                tiles_to_potentially_move.append(iter_tile)

            nexttile = self.get_location_dir(iter_tile, direc)
            if nexttile not in tiles_checked:
                tiles_to_check.append(nexttile)

            linked_tile = None
            if nexttile.type == "[":
                linked_tile = self.get_location_dir(nexttile, Direction.RIGHT)
                assert linked_tile.type == "]"
            elif nexttile.type == "]":
                linked_tile = self.get_location_dir(nexttile, Direction.LEFT)
                assert linked_tile.type == "["

            if linked_tile:
                if linked_tile not in tiles_checked:
                    tiles_to_check.append(linked_tile)

        while tiles_to_potentially_move:
            self.move_object(tiles_to_potentially_move.pop(-1), direc)

    def gps(self) -> int:
        checksum = 0

        for tile in self.tiles_by_type["["]:
            checksum += (tile.row - 1) * 100 + (tile.col - 1)

        return checksum


def calculate_solution(input_values: InputType) -> int:
    soko = WideSokoban(input_values[0])

    for direction in input_values[1]:
        soko.move(direction)

    return soko.gps()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
