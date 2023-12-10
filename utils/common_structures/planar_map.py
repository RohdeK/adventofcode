from collections import defaultdict, deque
from dataclasses import dataclass
from enum import IntEnum
from typing import Deque, Dict, List, Optional, Tuple


Position = Tuple[int, int]


@dataclass
class Located:
    row: int
    col: int

    def position(self) -> Position:
        return self.row, self.col

    def __eq__(self, other: "Located") -> bool:
        return self.row == other.row and self.col == other.col


@dataclass
class Location(Located):
    type: str


class Direction(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def shift(self, value: int) -> "Direction":
        return Direction((self.value + value) % 4)

    def next_clockwise(self) -> "Direction":
        return self.shift(1)

    def next_counter_clockwise(self) -> "Direction":
        return self.shift(3)


class PlanarMap:
    def __init__(self, locations: List[Location]):
        self.tiles = locations

        self.tiles_by_row: Dict[int, Deque[Location]] = defaultdict(deque)
        self.tiles_by_col: Dict[int, Deque[Location]] = defaultdict(deque)
        self.tiles_by_loc: Dict[Position, Location] = {}

        for tile in self.tiles:
            self.tiles_by_row[tile.row].append(tile)
            self.tiles_by_col[tile.col].append(tile)
            self.tiles_by_loc[(tile.row, tile.col)] = tile

    def __repr__(self) -> str:
        min_row = min(self.tiles_by_row.keys())
        max_row = max(self.tiles_by_row.keys())
        min_col = min(self.tiles_by_col.keys())
        max_col = max(self.tiles_by_col.keys())

        representation = ""

        for row in range(min_row, max_row + 1):
            for col in range(min_col, max_col + 1):
                tile_rep = self.tile_special_repr((row, col))
                tile = self.tiles_by_loc.get((row, col))

                if tile_rep is not None:
                    representation += tile_rep
                elif tile is None:
                    representation += " "
                else:
                    representation += tile.type

            representation += "\n"

        return representation

    def get_location(self, row: int, col: int) -> Location:
        return self.tiles_by_loc.get((row, col), None)

    def get_location_north(self, loc: Located) -> Optional[Location]:
        return self.tiles_by_loc.get((loc.row - 1, loc.col))

    def get_location_south(self, loc: Located) -> Optional[Location]:
        return self.tiles_by_loc.get((loc.row + 1, loc.col))

    def get_location_west(self, loc: Located) -> Optional[Location]:
        return self.tiles_by_loc.get((loc.row, loc.col - 1))

    def get_location_east(self, loc: Located) -> Optional[Location]:
        return self.tiles_by_loc.get((loc.row, loc.col + 1))

    def get_location_northeast(self, loc: Located) -> Optional[Location]:
        return self.tiles_by_loc.get((loc.row - 1, loc.col + 1))

    def get_location_northwest(self, loc: Located) -> Optional[Location]:
        return self.tiles_by_loc.get((loc.row - 1, loc.col - 1))

    def get_location_southeast(self, loc: Located) -> Optional[Location]:
        return self.tiles_by_loc.get((loc.row + 1, loc.col + 1))

    def get_location_southwest(self, loc: Located) -> Optional[Location]:
        return self.tiles_by_loc.get((loc.row + 1, loc.col - 1))

    def surrounding(self, loc: Located) -> List[Location]:
        return [tile for tile in (
            self.get_location_north(loc),
            self.get_location_northeast(loc),
            self.get_location_east(loc),
            self.get_location_southeast(loc),
            self.get_location_south(loc),
            self.get_location_southwest(loc),
            self.get_location_west(loc),
            self.get_location_northwest(loc),
        ) if tile]

    def tile_special_repr(self, location: Position) -> Optional[str]:
        return None


def parse_map_lines(input_lines: str) -> List[Location]:
    locations = []
    actual_lines = input_lines.split("\n")
    actual_lines = [line for line in actual_lines if line]

    for row_index_minus_one, line in enumerate(actual_lines):
        for col_index_minus_one, content in enumerate(line):
            locations.append(Location(
                col=col_index_minus_one + 1,
                row=row_index_minus_one + 1,
                type=content,
            ))

    return locations
