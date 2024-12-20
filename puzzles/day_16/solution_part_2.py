from bisect import bisect
from collections import deque
from typing import Optional

from puzzles.day_16.load_inputs import input_reader, InputType
from puzzles.day_16.solution_part_1 import Finished, RaceMap
from utils.common_structures.planar_map import Location


class VisitorRaceMap(RaceMap):
    def __init__(self, locations: InputType):
        super().__init__(locations)
        self.tiles_visited = deque()

    def splice(self) -> "VisitorRaceMap":
        spliced: RaceMap = super().splice()
        spliced.tiles_visited = self.tiles_visited.copy()
        return spliced

    def step_forward(self) -> Optional[Location]:
        tile = super().step_forward()
        if tile:
            self.tiles_visited.append(tile.position())
        return tile

    def race_until_finished(self) -> list["VisitorRaceMap"]:
        reindeer, _ = self.get_reindeer()
        finish_position = self.tiles_by_type["E"][0].position()

        distances = {reindeer.position(): 0}
        maps_still_in_race = [self]
        maps_scores = [self.score_accrued]
        shortest_paths = []

        def insert_racemap(racemap: VisitorRaceMap) -> None:
            nonlocal maps_still_in_race
            nonlocal maps_scores

            score = racemap.score_accrued
            i = bisect(maps_scores, score)
            maps_still_in_race.insert(i, racemap)
            maps_scores.insert(i, score)

        def update_distance(location: Optional[Location], racemap: VisitorRaceMap) -> None:
            nonlocal distances
            nonlocal maps_still_in_race
            nonlocal shortest_paths

            if location is None:
                return

            position = location.position()

            if position not in distances:
                print("Found first best for", position, racemap.score_accrued)
                distances[position] = racemap.score_accrued
                insert_racemap(racemap)
            elif distances[position] + 1000 >= racemap.score_accrued:
                print("Found new maybe best for", position, racemap.score_accrued)
                distances[position] = racemap.score_accrued
                insert_racemap(racemap)
            else:
                print("Dismissing", position, racemap.score_accrued)

            if position == finish_position:
                shortest_paths.append(racemap)

        while maps_still_in_race:
            starting_map = maps_still_in_race.pop(0)
            maps_scores.pop(0)

            forward_copy = starting_map.splice()
            update_distance(forward_copy.step_forward(), forward_copy)

            left_copy = starting_map.splice()
            update_distance(left_copy.step_left(), left_copy)

            right_copy = starting_map.splice()
            update_distance(right_copy.step_right(), right_copy)

        really_shortest_path = min(s.score_accrued for s in shortest_paths)

        return [p for p in shortest_paths if p.score_accrued == really_shortest_path]


def calculate_solution(input_values: InputType) -> int:
    for loc in input_values:
        if loc.type == "S":
            loc.type = ">"

    race = VisitorRaceMap(input_values)

    paths = race.race_until_finished()

    all_visited_locs = set()

    for path in paths:
        for loc in path.tiles_visited:
            all_visited_locs.add(loc)

    return len(all_visited_locs) + 1


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
