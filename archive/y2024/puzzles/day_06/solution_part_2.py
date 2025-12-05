from collections import deque
from typing import Iterator

from archive.y2024.puzzles.day_06.load_inputs import input_reader, InputType
from archive.y2024.puzzles.day_06.solution_part_1 import GuardMap
from utils.common_structures.planar_map import Direction, Location


class DynamicGuardMap(GuardMap):
    def __init__(self, locations: list[Location]):
        super().__init__(locations)
        guard_start = self.get_guard_tile()
        self.on_visit_facing = deque([Direction.from_tile_rep(guard_start.type)])
        self.looping_options = set()

    def guard_moves_to(self, loc: Location) -> None:
        # self.check_possible_full_loop(loc)
        super().guard_moves_to(loc)
        self.check_possible_early_loop(loc)
        self.on_visit_facing.append(Direction.from_tile_rep(loc.type))

    def check_possible_early_loop(self, guard_tile: Location) -> None:
        current_direction = Direction.from_tile_rep(guard_tile.type)
        direction_on_instant_turn = current_direction.next_clockwise()
        original_blockage = self.get_location_dir(guard_tile, current_direction)

        if original_blockage is None:
            return
        if original_blockage.position() in self.looping_options:
            return

        iter_tile = guard_tile
        max_iterations = 1000

        while True:
            max_iterations -= 1
            if max_iterations == 0:
                raise RuntimeError("Looped too long")

            next_on_early_turn = self.get_location_dir(iter_tile, direction_on_instant_turn)

            if next_on_early_turn is None:
                break

            if self.is_obstacle(next_on_early_turn):
                break

            next_pos = next_on_early_turn.position()
            if next_pos in self.visited_locations:
                start = 0
                for _ in range(self.visited_locations.count(next_pos)):
                    visit_index = self.visited_locations.index(next_pos, start)
                    start = visit_index
                    face_before = self.on_visit_facing[visit_index]
                    if face_before == direction_on_instant_turn:
                        self.looping_options.add(original_blockage.position())
                        # self.debug_print_loop(original_blockage)

            iter_tile = next_on_early_turn

    def check_possible_full_loop(self, loc: Location) -> None:
        if loc.position() not in self.visited_locations:
            return

        start = 0
        for _ in range(self.visited_locations.count(loc.position())):
            visited_index = self.visited_locations.index(loc.position(), start)
            face_before = self.on_visit_facing[visited_index]
            start = visited_index
            face_now = Direction.from_tile_rep(self.get_guard_tile().type)

            if face_now.next_clockwise() != face_before:
                return

            possible_next = self.get_location_dir(loc, face_now)

            if self.is_obstacle(possible_next):
                return

            self.looping_options.add(possible_next.position())
            # self.debug_print_loop(possible_next)

    def debug_print_loop(self, o_tile: Location) -> None:
        for i in self.visited_locations:
            if self.tiles_by_loc[i].type == ".":
                self.change_type(self.tiles_by_loc[i], "+")
        self.change_type(o_tile, "O")

        print(self)

        for i in self.visited_locations:
            if self.tiles_by_loc[i].type == "+":
                self.change_type(self.tiles_by_loc[i], ".")
        self.change_type(o_tile, ".")


class GuardIsLooping(Exception):
    pass


class BruteForceGuardMap(GuardMap):
    def __init__(self, locations: list[Location]):
        super().__init__(locations)
        guard_start = self.get_guard_tile()
        self.on_visit_facing = deque([Direction.from_tile_rep(guard_start.type)])

    def guard_moves_to(self, loc: Location) -> None:
        super().guard_moves_to(loc)

        if self.is_looping():
            raise GuardIsLooping()

        self.on_visit_facing.append(Direction.from_tile_rep(loc.type))

    def get_previous_visits(self, location: Location) -> Iterator[Direction]:
        start = 0
        for _ in range(self.visited_locations.count(location.position())):
            visit_index = self.visited_locations.index(location.position(), start)
            start = visit_index
            yield self.on_visit_facing[visit_index]

    def has_traversed(self, loc: Location) -> bool:
        return loc.position() in self.visited_locations

    def is_looping(self) -> bool:
        guard_tile = self.get_guard_tile()

        if guard_tile is None:
            return False

        next_tile = self.tile_in_front()

        if next_tile is None:
            return False

        for previous_dir in self.get_previous_visits(next_tile):
            if previous_dir == Direction.from_tile_rep(guard_tile.type):
                return True

        return False

    def tick_and_find_loops(self):
        postitions_which_loop = set()

        while self.guard_in_lab():
            possible_obstacle = self.tile_in_front()

            if possible_obstacle and not self.is_obstacle(possible_obstacle):
                if not self.has_traversed(possible_obstacle):
                    spliced = self.splice()
                    actual_obstacle = spliced.tile_in_front()
                    spliced.change_type(actual_obstacle, "#")

                    try:
                        spliced.tick_until_guard_leaves()
                    except GuardIsLooping:
                        print("Found a loop!")
                        postitions_which_loop.add(actual_obstacle.position())

            print("Could tick next.")
            self.tick()

        return postitions_which_loop


def calculate_solution(input_values: InputType) -> int:
    lab_map = BruteForceGuardMap(input_values)

    loops = lab_map.tick_and_find_loops()

    return len(loops)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
