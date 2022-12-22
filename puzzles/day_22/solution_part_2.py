from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Deque, Dict, List, Tuple

from puzzles.day_22.load_inputs import Located, Location, input_reader, InputType
from puzzles.day_22.solution_part_1 import Direction, Map


@dataclass
class FacettedLocation(Location):
    facet: int


class CubedMap(Map):
    def __init__(
        self,
        locations: List[Location],
        facet_appearance: List[List[int]],
        facet_movements: Dict[int, Dict[Direction, Tuple[int, Direction]]],
        facet_dim: int,
    ):
        self.facet_dim = facet_dim
        self.facet_appearance = facet_appearance
        self.facet_movements = facet_movements
        self.facets_by_loc = self.facet_locations(locations)
        self.tiles_by_facet: Dict[int, Deque[Location]] = defaultdict(deque)

        super().__init__(locations)

        for tile in self.tiles:
            self.tiles_by_facet[self.facets_by_loc[(tile.row, tile.col)]].append(tile)

        self.state_history = {}

    def perform_step(self) -> None:
        self.state_history[(self.state.row, self.state.col)] = self.state.direction
        super().perform_step()
        self.state_history[(self.state.row, self.state.col)] = self.state.direction

    def __repr__(self) -> None:
        max_rows = max(self.tiles_by_row.keys())
        max_cols = max(self.tiles_by_col.keys())

        representation = ""

        for row in range(max_rows + 1):
            for col in range(max_cols + 1):
                if (row, col) in self.state_history:
                    representation += {
                        Direction.RIGHT: ">",
                        Direction.LEFT: "<",
                        Direction.UP: "^",
                        Direction.DOWN: "v",
                    }[self.state_history[(row, col)]]
                    continue

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

    def facet_locations(self, locations: List[Location]) -> Dict[Tuple[int, int], int]:
        facetted_locations = {}

        for tile in locations:
            facet_col_index = (tile.col - 1) // self.facet_dim
            facet_row_index = (tile.row - 1) // self.facet_dim

            facet = self.facet_appearance[facet_row_index][facet_col_index]
            facetted_locations[(tile.row, tile.col)] = facet

        return facetted_locations

    def relative(self, tile: Located) -> Tuple[int, int]:
        return (tile.row - 1) % self.facet_dim, (tile.col - 1) % self.facet_dim

    def wrap_around(self) -> Location:
        next_row, next_col = self.state.row, self.state.col
        current_facet = self.facets_by_loc[(next_row, next_col)]

        next_facet, direction_shift = self.facet_movements[current_facet][self.state.direction]
        relative_row, relative_col = self.relative(self.state)

        if direction_shift == 1:
            if self.state.direction in (Direction.DOWN, Direction.UP):
                next_relative_row = self.facet_dim - 1 - relative_col
                next_relative_col = relative_row
            else:
                next_relative_row = relative_col
                next_relative_col = self.facet_dim - 1 - relative_row
        elif direction_shift == 2:
            if self.state.direction in (Direction.DOWN, Direction.UP):
                next_relative_row = relative_row
                next_relative_col = self.facet_dim - 1 - relative_col
            else:
                next_relative_row = self.facet_dim - 1 - relative_row
                next_relative_col = relative_col
        elif direction_shift == 3:
            if self.state.direction in (Direction.DOWN, Direction.UP):
                next_relative_row = relative_col
                next_relative_col = self.facet_dim - 1 - relative_row
            else:
                next_relative_row = self.facet_dim - 1 - relative_col
                next_relative_col = relative_row
        else:
            raise ValueError(next_facet, direction_shift)

        next_wrapped = next(tile for tile in self.tiles_by_facet[next_facet] if self.relative(tile) == (next_relative_row, next_relative_col))

        print(f"Moving from ({next_row}, {next_col})[{current_facet}] to ({next_wrapped.row}, {next_wrapped.col})[{next_facet}].")

        if next_wrapped.is_empty():
            self.state.direction = self.state.direction.shift(direction_shift)

        return next_wrapped

def calculate_solution(
    input_values: InputType,
    facets: List[List[int]],
    facet_movements: Dict[int, Dict[Direction, Tuple[int, int]]],
    facet_dim: int,
) -> int:
    locations, directions = input_values
    movement_game = CubedMap(locations, facets, facet_movements, facet_dim)
    movement_game.perform_moves(directions)
    state = movement_game.state
    print(movement_game)
    return state.row * 1000 + state.col * 4 + state.direction


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
