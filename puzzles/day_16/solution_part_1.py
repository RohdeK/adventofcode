from bisect import bisect
from typing import Optional

from puzzles.day_16.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Direction, Location, PlanarMap


class Finished(Exception):
    pass


class RaceMap(PlanarMap):
    def __init__(self, locations: InputType):
        super().__init__(locations)
        self.score_accrued = 0

    def splice(self) -> "RaceMap":
        spliced: RaceMap = super().splice()
        spliced.score_accrued = self.score_accrued
        return spliced

    def get_reindeer(self) -> tuple[Location, Direction]:
        reindeer = [
            *self.tiles_by_type.get("<", []),
            *self.tiles_by_type.get(">", []),
            *self.tiles_by_type.get("v", []),
            *self.tiles_by_type.get("^", []),
        ][0]

        direction = Direction.from_tile_rep(reindeer.type)

        return reindeer, direction

    def step_left(self) -> Optional[Location]:
        self.turn(False)
        return self.step_forward()

    def step_right(self) -> Optional[Location]:
        self.turn(True)
        return self.step_forward()

    def step_forward(self) -> Optional[Location]:
        reindeer, direction = self.get_reindeer()

        next_tile = self.get_location_dir(reindeer, direction)

        if next_tile.type == "#":
            return None

        assert next_tile.type in (".", "E")

        self.change_type(next_tile, reindeer.type)
        self.change_type(reindeer, ".")

        self.score_accrued += 1

        return next_tile

    def turn(self, clockwise: bool = True) -> Location:
        reindeer, direction = self.get_reindeer()

        if clockwise:
            next_direction = direction.next_clockwise()
        else:
            next_direction = direction.next_counter_clockwise()

        self.change_type(reindeer, next_direction.to_tile_rep())

        self.score_accrued += 1000

        return reindeer

    def race_until_finished(self) -> int:
        reindeer, _ = self.get_reindeer()
        finish_position = self.tiles_by_type["E"][0].position()

        distances = {reindeer.position(): 0}
        maps_still_in_race = [self]
        maps_scores = [self.score_accrued]

        def insert_racemap(racemap: RaceMap) -> None:
            nonlocal maps_still_in_race
            nonlocal maps_scores

            score = racemap.score_accrued
            i = bisect(maps_scores, score)
            maps_still_in_race.insert(i, racemap)
            maps_scores.insert(i, score)

        def update_distance(location: Optional[Location], racemap: RaceMap) -> None:
            nonlocal distances
            nonlocal maps_still_in_race

            if location is None:
                return

            position = location.position()

            if position not in distances:
                print("Found first best for", position, racemap.score_accrued)
                distances[position] = racemap.score_accrued
                insert_racemap(racemap)
            elif distances[position] >= racemap.score_accrued:
                print("Found new best for", position, racemap.score_accrued)
                distances[position] = racemap.score_accrued
                insert_racemap(racemap)
            else:
                print("Dismissing", position, racemap.score_accrued)

            if position == finish_position:
                raise Finished()
        try:
            while maps_still_in_race:
                starting_map = maps_still_in_race.pop(0)
                maps_scores.pop(0)

                forward_copy = starting_map.splice()
                update_distance(forward_copy.step_forward(), forward_copy)

                left_copy = starting_map.splice()
                update_distance(left_copy.step_left(), left_copy)

                right_copy = starting_map.splice()
                update_distance(right_copy.step_right(), right_copy)
        except Finished:
            return distances[finish_position]


def calculate_solution(input_values: InputType) -> int:
    for loc in input_values:
        if loc.type == "S":
            loc.type = ">"

    race = RaceMap(input_values)

    return race.race_until_finished()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
