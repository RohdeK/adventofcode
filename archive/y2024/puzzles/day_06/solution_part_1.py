from collections import deque
from typing import Optional

from archive.y2024.puzzles.day_06.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Direction, Location, PlanarMap


class GuardMap(PlanarMap):
    def __init__(self, locations: list[Location]):
        super().__init__(locations)
        guard_start = self.get_guard_tile()
        self.visited_locations = deque([guard_start.position()])

    def guard_in_lab(self) -> bool:
        return self.get_guard_tile() is not None

    def get_guard_tile(self) -> Optional[Location]:
        for direc in Direction:
            if guard_tile := self.get_one_by_type(direc.to_tile_rep()):
                return guard_tile

    def tile_in_front(self) -> Location:
        guard_tile = self.get_guard_tile()
        facing = Direction.from_tile_rep(guard_tile.type)
        return self.get_location_dir(guard_tile, facing)

    def tick_until_guard_leaves(self):
        while self.guard_in_lab():
            self.tick()

    def guard_turns_right(self) -> None:
        guard_tile = self.get_guard_tile()
        facing = Direction.from_tile_rep(guard_tile.type)
        facing_next = facing.next_clockwise()
        self.change_type(guard_tile, facing_next.to_tile_rep())

    def guard_moves_to(self, location: Location) -> None:
        assert not self.is_obstacle(location)
        guard_tile = self.get_guard_tile()
        current_facing = guard_tile.type

        self.change_type(guard_tile, ".")
        self.change_type(location, current_facing)

        self.visited_locations.append(location.position())

    def guard_leaves(self) -> None:
        guard_tile = self.get_guard_tile()
        self.change_type(guard_tile, ".")

    @staticmethod
    def is_obstacle(location: Location) -> bool:
        return location.type == "#"

    def tick(self) -> None:
        next_tile = self.tile_in_front()

        if next_tile is None:
            self.guard_leaves()

        elif self.is_obstacle(next_tile):
            self.guard_turns_right()

        else:
            self.guard_moves_to(next_tile)


def calculate_solution(input_values: InputType) -> int:
    lab_map = GuardMap(input_values)

    lab_map.tick_until_guard_leaves()

    return len(set(lab_map.visited_locations))


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
