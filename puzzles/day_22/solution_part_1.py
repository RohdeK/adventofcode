from collections import defaultdict, deque
from dataclasses import dataclass
from enum import Enum
from typing import Deque, Dict, List, Optional, Tuple

from puzzles.day_22.load_inputs import Located, Location, Movement, Turn, Walk, input_reader, InputType


class Direction(int, Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

    def shift(self, clockwise_by: int) -> "Direction":
        return Direction((self.value + clockwise_by) % 4)

    def next_clockwise(self) -> "Direction":
        return self.shift(1)

    def next_counter_clockwise(self) -> "Direction":
        return self.shift(3)


@dataclass
class PersonState(Located):
    direction: Direction


class Map:
    def __init__(self, tiles: List[Location]):
        self.tiles = [tile for tile in tiles if not tile.is_abyss()]

        self.tiles_by_row: Dict[int, Deque[Location]] = defaultdict(deque)
        self.tiles_by_col: Dict[int, Deque[Location]] = defaultdict(deque)
        self.tiles_by_loc: Dict[Tuple[int, int], Location] = {}

        for tile in self.tiles:
            self.tiles_by_row[tile.row].append(tile)
            self.tiles_by_col[tile.col].append(tile)
            self.tiles_by_loc[(tile.row, tile.col)] = tile

        starting_col = min(tile.col for tile in self.tiles_by_row[1])
        self.state = PersonState(row=1, col=starting_col, direction=Direction.RIGHT)

    def perform_moves(self, moves: List[Movement]) -> None:
        for move in moves:
            self.perform_move(move)

    def perform_move(self, move: Movement) -> None:
        if isinstance(move, Turn):
            self.perform_turn(move.direction)
        elif isinstance(move, Walk):
            self.perform_walk(move.distance)
        else:
            raise ValueError(move)

    def perform_turn(self, dir_desc: str) -> None:
        if dir_desc == "L":
            self.state.direction = self.state.direction.next_counter_clockwise()
        elif dir_desc == "R":
            self.state.direction = self.state.direction.next_clockwise()
        else:
            raise ValueError(dir_desc)

    def perform_walk(self, distance: int) -> None:
        for i in range(distance):
            self.perform_step()

    def perform_step(self) -> None:
        next_tile = self.next_tile()

        if next_tile.is_rock():
            pass
        elif next_tile.is_empty():
            self.state.row, self.state.col = next_tile.row, next_tile.col
        else:
            raise ValueError(next_tile.type)

    def next_tile(self) -> Location:
        next_row, next_col = self.state.row, self.state.col
        next_row += {Direction.DOWN: 1, Direction.UP: -1}.get(self.state.direction, 0)
        next_col += {Direction.RIGHT: 1, Direction.LEFT: -1}.get(self.state.direction, 0)

        next_tile = self.get_tile_at(next_row, next_col)

        if next_tile is None:
            next_tile = self.wrap_around()

        return next_tile

    def wrap_around(self) -> Location:
        next_row, next_col = self.state.row, self.state.col

        if self.state.direction == Direction.DOWN:
            next_row = min(tile.row for tile in self.tiles_by_col[self.state.col])
        elif self.state.direction == Direction.UP:
            next_row = max(tile.row for tile in self.tiles_by_col[self.state.col])
        elif self.state.direction == Direction.RIGHT:
            next_col = min(tile.col for tile in self.tiles_by_row[self.state.row])
        elif self.state.direction == Direction.LEFT:
            next_col = max(tile.col for tile in self.tiles_by_row[self.state.row])

        return self.get_tile_at(next_row, next_col)

    def get_tile_at(self, row: int, col: int) -> Optional[Location]:
        return self.tiles_by_loc.get((row, col))


def calculate_solution(input_values: InputType) -> int:
    locations, directions = input_values
    movement_game = Map(locations)
    movement_game.perform_moves(directions)
    state = movement_game.state
    return state.row * 1000 + state.col * 4 + state.direction


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
