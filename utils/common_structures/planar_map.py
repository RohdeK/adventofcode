from collections import defaultdict, deque
from dataclasses import dataclass
from enum import IntEnum
from typing import Deque, Dict, List, Optional, Self, Tuple


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

    def copy(self) -> "Location":
        return Location(
            row=self.row,
            col=self.col,
            type=self.type,
        )


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def shift(self, value: int) -> "Direction":
        return Direction((self.value + value) % 4)

    def next_clockwise(self) -> "Direction":
        return self.shift(1)

    def next_counter_clockwise(self) -> "Direction":
        return self.shift(3)

    def to_tile_rep(self) -> str:
        return {
            Direction.LEFT: "<",
            Direction.RIGHT: ">",
            Direction.DOWN: "v",
            Direction.UP: "^",
        }[self]

    @classmethod
    def from_tile_rep(cls, tile_rep: str) -> "Direction":
        return {
            "<": Direction.LEFT,
            ">": Direction.RIGHT,
            "v": Direction.DOWN,
            "^": Direction.UP,
        }[tile_rep]


class PlanarMap:
    def __init__(self, locations: List[Location]):
        self.tiles = locations

        self.tiles_by_row: Dict[int, Deque[Location]] = defaultdict(deque)
        self.tiles_by_col: Dict[int, Deque[Location]] = defaultdict(deque)
        self.tiles_by_loc: Dict[Position, Location] = {}
        self.tiles_by_type: Dict[str, Deque[Location]] = defaultdict(deque)

        for tile in self.tiles:
            self.tiles_by_row[tile.row].append(tile)
            self.tiles_by_col[tile.col].append(tile)
            self.tiles_by_loc[(tile.row, tile.col)] = tile
            self.tiles_by_type[tile.type].append(tile)

        self.max_row = max(self.tiles_by_row.keys())
        self.max_col = max(self.tiles_by_col.keys())

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

    def splice(self) -> Self:
        return self.__class__([tile.copy() for tile in self.tiles])

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

    def get_location_to(self, loc: Located, direction: str) -> Optional[Location]:
        return {
            "north": self.get_location_north,
            "northwest": self.get_location_northwest,
            "west": self.get_location_west,
            "southwest": self.get_location_southwest,
            "south": self.get_location_south,
            "southeast": self.get_location_southeast,
            "east": self.get_location_east,
            "northeast": self.get_location_northeast,
        }[direction](loc)

    def get_location_dir(self, loc: Located, direction: Direction) -> Optional[Location]:
        return {
            Direction.UP: self.get_location_north,
            Direction.DOWN: self.get_location_south,
            Direction.LEFT: self.get_location_west,
            Direction.RIGHT: self.get_location_east,
        }[direction](loc)

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

    def row_indices(self) -> List[int]:
        return sorted(self.tiles_by_row.keys())

    def col_indices(self) -> List[int]:
        return sorted(self.tiles_by_col.keys())

    def change_type(self, loc: Location, to_type: str) -> None:
        self.tiles_by_type[loc.type].remove(loc)
        self.tiles_by_type[to_type].append(loc)
        loc.type = to_type

    def get_one_by_type(self, by_type: str) -> Optional[Location]:
        tiles = self.tiles_by_type.get(by_type, [])

        if len(tiles) == 0:
            return None
        elif len(tiles) == 1:
            return tiles[0]
        else:
            raise RuntimeError(f"More than 1 tiles for {by_type} found: {tiles}.")


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
