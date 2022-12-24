from collections import defaultdict, deque
from typing import Deque, Dict, List, Optional

from puzzles.day_24.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Location, PlanarMap, Position


class BlizzardMap(PlanarMap):
    def __init__(self, locations: List[Location]):
        self.min_row = 1
        self.max_row = max(loc.row for loc in locations)
        self.min_col = 1
        self.max_col = max(loc.col for loc in locations)

        self.starting_col = next(tile.col for tile in locations if tile.row == self.min_row and tile.type == ".")
        self.ending_col = next(tile.col for tile in locations if tile.row == self.max_row and tile.type == ".")
        starting_state: Position = (self.min_row, self.starting_col)
        self.target_state: Position = (self.max_row, self.ending_col)

        self.possible_states = deque()
        self.possible_states.append(starting_state)

        self.time_passed = 0

        super().__init__([loc for loc in locations if loc.type != "."])
        self.tiles_by_loc: Dict[Position, Deque[Location]] = defaultdict(deque)

        for tile in self.tiles:
            self.tiles_by_loc[(tile.row, tile.col)].append(tile)

    def run_until_done(self) -> int:
        while not self.next_round():
            pass

        return self.time_passed

    def next_round(self) -> bool:
        self.move_all_blizzards()

        next_run_states = deque()

        for state in self.possible_states:
            for location in self.list_moves(state):
                if location == self.target_state:
                    return True

                next_run_states.append(location)

            if self.tiles_by_loc.get(state) is None:
                next_run_states.append(state)

        self.possible_states = next_run_states

        self.time_passed += 1

        return False

    def tile_special_repr(self, location: Position) -> Optional[str]:
        if location in self.possible_states:
            return "E"

        all_tiles_on_loc = [tile for tile in self.tiles if tile.position() == location]

        if len(all_tiles_on_loc) == 1:
            return all_tiles_on_loc[0].type
        elif len(all_tiles_on_loc) == 0:
            return "."
        else:
            return str(len(all_tiles_on_loc))

    def move_all_blizzards(self) -> None:
        for tile in self.tiles:
            self.tiles_by_loc[(tile.row, tile.col)].remove(tile)
            next_col = tile.col
            next_row = tile.row

            if tile.type == ">":
                next_col = tile.col + 1
                if next_col == self.max_col:
                    next_col = self.min_col + 1
            if tile.type == "<":
                next_col = tile.col - 1
                if next_col == self.min_col:
                    next_col = self.max_col - 1
            if tile.type == "^":
                next_row = tile.row - 1
                if next_row == self.min_row:
                    if next_col == self.starting_col:
                        pass
                    elif next_col == self.ending_col:
                        next_row = self.max_row
                    else:
                        next_row = self.max_row - 1
            if tile.type == "v":
                next_row = tile.row + 1
                if next_row == self.max_row:
                    if next_col == self.ending_col:
                        pass
                    elif next_col == self.starting_col:
                        next_row = self.min_row
                    else:
                        next_row = self.min_row + 1

            tile.row = next_row
            tile.col = next_col

            self.tiles_by_loc[(tile.row, tile.col)].append(tile)

    def list_moves(self, based_on_state: Position) -> List[Position]:
        empties = []

        for position in self.surrounding_positions(based_on_state):
            if self.tiles_by_loc.get(position) is None:
                empties.append(position)

        return empties

    @staticmethod
    def surrounding_positions(of_position: Position) -> List[Position]:
        base_row, base_col = of_position

        return [
            (base_row - 1, base_col - 1),
            (base_row - 1, base_col),
            (base_row - 1, base_col + 1),
            (base_row, base_col - 1),
            (base_row, base_col + 1),
            (base_row + 1, base_col - 1),
            (base_row + 1, base_col),
            (base_row + 1, base_col + 1),
        ]


    def move_to(self) -> List[Position]:
        pass

def calculate_solution(input_values: InputType) -> int:
    bliz = BlizzardMap(input_values[0])
    time_passed = bliz.run_until_done()
    return time_passed


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
