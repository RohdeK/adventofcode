from collections import deque
from dataclasses import dataclass
from enum import IntEnum
from typing import Deque, Dict, Iterator, List, Optional, Tuple

from puzzles.day_22.load_inputs import Located, Location
from puzzles.day_23.load_inputs import InputType, input_reader


@dataclass
class Elf(Located):
    intended_next_position: Tuple[int, int]


class Direction(IntEnum):
    NORTH = 0
    SOUTH = 1
    WEST = 2
    EAST = 3

    def shift(self, value: int) -> "Direction":
        return Direction((self.value + value) % 4)


class ElvesDanceMap:
    def __init__(self, tiles: List[Location]):
        tiles = [tile for tile in tiles if not tile.is_abyss()]
        self.tiles_by_loc: Dict[Tuple[int, int], Location] = {}
        self.elves: Deque[Elf] = deque()
        self.direction_modifier = 0

        for tile in tiles:
            self.tiles_by_loc[(tile.row, tile.col)] = tile
            if tile.type == "#":
                self.elves.append(Elf(
                    intended_next_position=None,
                    row=tile.row,
                    col=tile.col,
                ))

    def __repr__(self) -> None:
        min_row = min(row for row, col in self.tiles_by_loc.keys())
        max_row = max(row for row, col in self.tiles_by_loc.keys())
        min_col = min(col for row, col in self.tiles_by_loc.keys())
        max_col = max(col for row, col in self.tiles_by_loc.keys())

        representation = ""

        for row in range(min_row, max_row + 1):
            for col in range(min_col, max_col + 1):
                tile = self.tiles_by_loc.get((row, col))
                if tile is None:
                    representation += " "
                elif tile.is_empty():
                    representation += "."
                elif tile.is_rock():
                    representation += "#"
                else:
                    raise ValueError(tile.type)

            representation += "\n"

        return representation

    def get_location(self, row: int, col: int) -> Location:
        location = self.tiles_by_loc.get((row, col), None)

        if location is None:
            location = Location(row=row, col=col, type=".")
            self.tiles_by_loc[(row, col)] = location

        return location

    def perform_rounds(self, num_rounds: int) -> None:
        for _ in range(num_rounds):
            self.perform_round()

    def perform_round(self) -> None:
        for elf in self.elves:
            elf.intended_next_position = self.determine_intent(elf)

        for elf in self.elves:
            self.act_on_intent(elf)

        self.direction_modifier += 1

    def direction_order(self) -> Iterator[Direction]:
        for direction in (
            Direction.NORTH,
            Direction.SOUTH,
            Direction.WEST,
            Direction.EAST
        ):
            yield direction.shift(self.direction_modifier)

    def jitter_in_direction(self, from_loc: Location, direc: Direction) -> List[Location]:
        if direc == Direction.NORTH:
            return [self.get_location(from_loc.row - 1, from_loc.col + mod) for mod in (-1, 0, 1)]
        elif direc == Direction.SOUTH:
            return [self.get_location(from_loc.row + 1, from_loc.col + mod) for mod in (-1, 0, 1)]
        elif direc == Direction.WEST:
            return [self.get_location(from_loc.row + mod, from_loc.col - 1) for mod in (-1, 0, 1)]
        elif direc == Direction.EAST:
            return [self.get_location(from_loc.row + mod, from_loc.col + 1) for mod in (-1, 0, 1)]

    def determine_intent(self, elf: Elf) -> Optional[Tuple[int, int]]:
        elf.intended_next_position = None

        possible_locations_by_prio = []

        for direc in self.direction_order():
            locations_to_check = self.jitter_in_direction(elf, direc)
            if all(loc.is_empty() for loc in locations_to_check):
                possible_locations_by_prio.append(
                    (locations_to_check[1].row, locations_to_check[1].col)
                )

        if len(possible_locations_by_prio) in (0, 4):
            return None
        else:
            return possible_locations_by_prio[0]

    def act_on_intent(self, elf: Elf) -> None:
        if elf.intended_next_position is None:
            return

        for other_elf in self.elves:
            if elf is other_elf:
                continue

            if elf.intended_next_position == other_elf.intended_next_position:
                elf.intended_next_position = None
                other_elf.intended_next_position = None

        if elf.intended_next_position is None:
            return

        current_tile = self.get_location(elf.row, elf.col)
        current_tile.type = "."

        elf.row, elf.col = elf.intended_next_position

        next_tile = self.get_location(elf.row, elf.col)
        next_tile.type = "#"

    def count_empty_spaces(self) -> int:
        min_elf_row = min(elf.row for elf in self.elves)
        max_elf_row = max(elf.row for elf in self.elves)
        min_elf_col = min(elf.col for elf in self.elves)
        max_elf_col = max(elf.col for elf in self.elves)

        row_dim = max_elf_row - min_elf_row + 1
        col_dim = max_elf_col - min_elf_col + 1

        num_locations_in_rectange = row_dim * col_dim
        num_empty_locations = num_locations_in_rectange - len(self.elves)

        return num_empty_locations


def calculate_solution(input_values: InputType) -> int:
    elves_map = ElvesDanceMap(input_values[0])

    elves_map.perform_rounds(10)

    return elves_map.count_empty_spaces()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
