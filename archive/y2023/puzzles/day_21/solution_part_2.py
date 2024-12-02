from dataclasses import dataclass
from typing import Dict, List, Optional

from puzzles.day_21.load_inputs import input_reader, InputType
from puzzles.day_21.solution_part_1 import GardenMap
from utils.common_structures.planar_map import Location, PlanarMap, Position


class InfiniteGardenMap(PlanarMap):
    def __init__(self, locations: List[Location]):
        super().__init__(locations)
        self.tile_min_distances_by_start_loc: Dict[Position, Dict[Position, int]] = {}

    def step_until_done(self, start_tile: Position) -> None:
        if start_tile in self.tile_min_distances_by_start_loc:
            return

        tile_min_distances = {}

        tiles_to_check = [self.tiles_by_loc[start_tile]]
        north_breakthrough = []

        step_num = 0
        while True:
            step_num += 1

            if len(tiles_to_check) == 0:
                break

            tiles_to_check_next_iteration = []

            for location in tiles_to_check:
                n_loc = self.get_location_north(location)
                if n_loc is None:
                    north_breakthrough.append((step_num, location.col))

                for loc in (
                    n_loc,
                    self.get_location_east(location),
                    self.get_location_west(location),
                    self.get_location_south(location),
                ):
                    if loc is None:
                        continue

                    if loc.type == "#":
                        continue

                    if loc.position() not in tile_min_distances:
                        tile_min_distances[loc.position()] = step_num
                        tiles_to_check_next_iteration.append(loc)

            tiles_to_check = tiles_to_check_next_iteration

        print(north_breakthrough)
        self.tile_min_distances_by_start_loc[start_tile] = tile_min_distances

    def step_all(self) -> None:
        self.step_until_done(self.tiles_by_type["S"][0].position())

        # self.step_until_done((1, 1))
        # self.step_until_done((1, self.max_col))
        # self.step_until_done((self.max_row, 1))
        # self.step_until_done((self.max_row, self.max_col))

        for row in self.row_indices():
            self.step_until_done((row, 1))
            self.step_until_done((row, self.max_col))

        for col in self.col_indices():
            self.step_until_done((1, col))
            self.step_until_done((self.max_row, col))

    def tile_special_repr(self, location: Position) -> Optional[str]:
        if location in self.tile_min_distances_by_start_loc[(6, 6)]:
            return "O"

    def get_locations_of_corner(self, num_steps: int, to_corner: Position) -> int:
        num_steps_mod = num_steps % 2
        distances_from_start = self.tile_min_distances_by_start_loc[
            self.tiles_by_type["S"][0].position()
        ]
        distance_to_corner = distances_from_start[to_corner] + 2

        num_even = sum(1 for v in distances_from_start.values() if v % 2 == 0)
        num_odd = sum(1 for v in distances_from_start.values() if v % 2 == 1)

        steps_beyond_corner = num_steps - distance_to_corner
        # Using row = col
        max_patches_diagonal = steps_beyond_corner // self.max_row
        tile_distances_opposite = self.tile_min_distances_by_start_loc[
            (self.max_row - to_corner[0] + 1, self.max_col - to_corner[1] + 1)
        ]

        num_locations = 0
        for patch_row in range(1, max_patches_diagonal + 1):
            for patch_col in range(1, patch_row + 1):
                patch_mod = (num_steps_mod + patch_row + patch_col) % 2
                if (
                    patch_col * self.max_col + patch_row * self.max_row
                    < steps_beyond_corner
                ):
                    # Case entire patch is in reach
                    num_locations += {
                        0: num_even,
                        1: num_odd,
                    }[patch_mod]
                else:
                    steps_in_last_segment = (
                        steps_beyond_corner
                        - (patch_row - 1) * self.max_row
                        - (patch_col - 1) * self.max_col
                    )
                    num_locations += sum(
                        1
                        for v in tile_distances_opposite.values()
                        if v <= steps_in_last_segment and v % 2 == patch_mod
                    )

        return num_locations

    def get_edge_travel_distances(self, edge_pos: Position) -> List[int]:
        distances_from_start = self.tile_min_distances_by_start_loc[
            self.tiles_by_type["S"][0].position()
        ]
        travel_distances = []
        edge_break = None

        while True:
            edge_breaks = {e: n for e, n in distances_from_start.items() if (edge_pos[0] == 0 and edge_pos[1] == e[1]) or (edge_pos[1] == 0 and edge_pos[0] == e[0])}
            travel_distance = min(edge_breaks.values())
            travel_distances.append(travel_distance)
            edge_breaks = [e for e, n in edge_breaks.items() if n == travel_distance]

            if len(edge_breaks) > 1:
                raise ValueError()

            if edge_breaks[0] == edge_break:
                break

            edge_break = edge_breaks[0]
            if edge_pos[0] == 0:
                next_start = edge_break[0], self.max_col - edge_break[1] + 1
            else:
                next_start = self.max_row - edge_break[0] + 1, edge_break[1]

            distances_from_start = self.tile_min_distances_by_start_loc[next_start]


        return travel_distances

    def get_locations_of_edge(self, num_steps: int, edge_pos: Position) -> int:
        distances_from_start = self.tile_min_distances_by_start_loc[
            self.tiles_by_type["S"][0].position()
        ]
        num_steps_mod = num_steps % 2

        edge_distances = self.get_edge_travel_distances(edge_pos)

        distance_to_edge = edge_distances.pop(0) + 1

        num_even = sum(1 for v in distances_from_start.values() if v % 2 == 0)
        num_odd = sum(1 for v in distances_from_start.values() if v % 2 == 1)

        steps_beyond_edge = num_steps - distance_to_edge
        # Using row = col
        max_patches_edge = steps_beyond_edge // self.max_row

        num_locations = 0
        travel_spent = 0
        for patch_dim in range(1, max_patches_edge + 1):
            patch_mod = (num_steps_mod + patch_dim) % 2

            if patch_dim <= len(edge_distances):
                travel_spent += edge_distances[patch_dim - 1]
            else:
                travel_spent += edge_distances[-1]

            if travel_spent < steps_beyond_edge - edge_distances[-1]:
                # Case entire patch is in reach
                num_locations += {
                    0: num_even,
                    1: num_odd,
                }[patch_mod]
            else:
                remaining_



def calculate_solution(input_values: InputType, num_steps: int) -> int:
    print("\n")
    gmap = InfiniteGardenMap(input_values[0])

    gmap.step_all()

    # for row in gmap.row_indices():
    #     col = 1
    #     print(gmap.tile_min_distances_by_start_loc[(1, gmap.max_col)][(row, col)])

    # print(gmap)

    locations_top_left = gmap.get_locations_of_corner(num_steps, (1, 1))
    locations_top_right = gmap.get_locations_of_corner(num_steps, (1, gmap.max_col))
    locations_bot_left = gmap.get_locations_of_corner(num_steps, (gmap.max_row, 1))
    locations_bot_right = gmap.get_locations_of_corner(num_steps, (gmap.max_row, gmap.max_col))

    locations_top = gmap.get_locations_of_edge(num_steps, (1, 0))
    locations_bot = gmap.get_locations_of_edge(num_steps, (gmap.max_row, 0))
    locations_left = gmap.get_locations_of_edge(num_steps, (0, 1))
    locations_right = gmap.get_locations_of_edge(num_steps, (0, gmap.max_col))

    locations_to_sum = [
        locations_bot_left,
        locations_bot_right,
        locations_top_left,
        locations_top_right,
        locations_right,
        locations_left,
        locations_bot,
        locations_top,
    ]

    return sum(locations_to_sum)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input, 26501365))
