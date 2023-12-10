from typing import Optional

from puzzles.day_10.load_inputs import input_reader, InputType
from puzzles.day_10.solution_part_1 import build_network
from utils.common_structures.planar_map import PlanarMap, Position


class NetworkMap(PlanarMap):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.network = build_network(self)
        self.network_map = {
            (loc.row, loc.col): loc for loc in self.network
        }

    def tile_special_repr(self, loc: Position) -> Optional[str]:
        tile = self.tiles_by_loc[loc]
        if loc in self.network_map:
            return f"\033[96m{tile.type}\033[0m"
        if tile.type == "X":
            return f"\033[93m{tile.type}\033[0m"
        if tile.type == "1":
            return f"\033[91m{tile.type}\033[0m"
        if tile.type == "2":
            return f"\033[94m{tile.type}\033[0m"


def remove_junk_tiles(pipe_map: NetworkMap) -> None:
    for tile in pipe_map.tiles:
        if tile.position() not in pipe_map.network_map:
            tile.type = "."


def iter_cover_outers(pipe_map: NetworkMap) -> None:
    something_changed = False

    for tile in pipe_map.tiles_by_row[min(pipe_map.tiles_by_row.keys())]:
        if tile.type == ".":
            tile.type = "O"
            something_changed = True

    for tile in pipe_map.tiles_by_row[max(pipe_map.tiles_by_row.keys())]:
        if tile.type == ".":
            tile.type = "O"
            something_changed = True

    for tile in pipe_map.tiles_by_col[min(pipe_map.tiles_by_col.keys())]:
        if tile.type == ".":
            tile.type = "O"
            something_changed = True

    for tile in pipe_map.tiles_by_col[max(pipe_map.tiles_by_col.keys())]:
        if tile.type == ".":
            tile.type = "O"
            something_changed = True

    tiles_with_dot = [t for t in pipe_map.tiles if t.type == "."]

    while something_changed:
        remaining_tiles_with_dot = []

        something_changed = False

        for tile in tiles_with_dot:
            if any(t.type == "O" for t in pipe_map.surrounding(tile)):
                tile.type = "O"
                something_changed = True
            else:
                remaining_tiles_with_dot.append(tile)

        tiles_with_dot = remaining_tiles_with_dot


def decide_inner_clusters(pipe_map: NetworkMap) -> None:
    something_changed = True

    while something_changed:
        tiles_with_dot = [t for t in pipe_map.tiles if t.type == "."]

        something_changed = False

        for dot_tile in tiles_with_dot:
            clustered_dots_to_check = [dot_tile]
            cluster_dots_checked = []
            dot_cluster_is_outside = False

            while clustered_dots_to_check:
                dot_tile = clustered_dots_to_check.pop()
                cluster_dots_checked.append(dot_tile)

                for tile in pipe_map.surrounding(dot_tile):
                    if tile.type == ".":
                        if tile not in cluster_dots_checked:
                            clustered_dots_to_check.append(tile)

                    elif not dot_cluster_is_outside and tile not in pipe_map.network:
                        dot_cluster_is_outside = True

            for tile in cluster_dots_checked:
                tile.type = "O" if dot_cluster_is_outside else "I"
                something_changed = True

            if something_changed:
                break


def traverse_and_categorize(pipe_map: NetworkMap) -> None:
    row_diff = pipe_map.network[0].row - pipe_map.network[-1].row
    col_diff = pipe_map.network[0].col - pipe_map.network[-1].col

    coming_from_map = {
        (1, 0): "north",
        (-1, 0): "south",
        (0, 1): "west",
        (0, -1): "east",
    }

    coming_from = coming_from_map[(row_diff, col_diff)]

    row_diff_2 = pipe_map.network[0].row - pipe_map.network[1].row
    col_diff_2 = pipe_map.network[0].col - pipe_map.network[1].col

    s_going_to = coming_from_map[(row_diff_2, col_diff_2)]

    s_value = {
        ("north", "south"): "|",
        ("north", "east"): "L",
        ("north", "west"): "J",
        ("south", "north"): "|",
        ("south", "west"): "7",
        ("south", "east"): "F",
        ("east", "west"): "-",
        ("east", "north"): "L",
        ("east", "south"): "F",
        ("west", "east"): "-",
        ("west", "north"): "J",
        ("west", "south"): "7",
    }[(coming_from, s_going_to)]

    for tile in pipe_map.network:
        current_type = tile.type
        if current_type == "S":
            current_type = s_value

        west_tile = pipe_map.get_location_west(tile)
        east_tile = pipe_map.get_location_east(tile)
        north_tile = pipe_map.get_location_north(tile)
        south_tile = pipe_map.get_location_south(tile)
        southwest_tile = pipe_map.get_location_southwest(tile)
        northeast_tile = pipe_map.get_location_northeast(tile)
        southeast_tile = pipe_map.get_location_southeast(tile)
        northwest_tile = pipe_map.get_location_northwest(tile)

        left_sides = []
        right_sides = []

        if current_type == "|":
            if coming_from == "south":
                left_sides.append(west_tile)
                right_sides.append(east_tile)
            elif coming_from == "north":
                left_sides.append(east_tile)
                right_sides.append(west_tile)
            else:
                raise ValueError(current_type, coming_from)

        elif current_type == "-":
            if coming_from == "west":
                left_sides.append(north_tile)
                right_sides.append(south_tile)
            elif coming_from == "east":
                left_sides.append(south_tile)
                right_sides.append(north_tile)
            else:
                raise ValueError(current_type, coming_from)

        elif current_type == "7":
            if coming_from == "south":
                left_sides.append(southwest_tile)
                right_sides.append(north_tile)
                right_sides.append(east_tile)
                right_sides.append(northeast_tile)
                coming_from = "east"
            elif coming_from == "west":
                left_sides.append(north_tile)
                left_sides.append(east_tile)
                left_sides.append(northeast_tile)
                right_sides.append(southwest_tile)
                coming_from = "north"
            else:
                raise ValueError(current_type, coming_from)

        elif current_type == "F":
            if coming_from == "south":
                left_sides.append(west_tile)
                left_sides.append(northwest_tile)
                left_sides.append(north_tile)
                right_sides.append(southeast_tile)
                coming_from = "west"
            elif coming_from == "east":
                left_sides.append(southeast_tile)
                right_sides.append(north_tile)
                right_sides.append(northwest_tile)
                right_sides.append(west_tile)
                coming_from = "north"
            else:
                raise ValueError(current_type, coming_from)

        elif current_type == "L":
            if coming_from == "north":
                left_sides.append(northeast_tile)
                right_sides.append(west_tile)
                right_sides.append(southwest_tile)
                right_sides.append(south_tile)
                coming_from = "west"
            elif coming_from == "east":
                right_sides.append(northeast_tile)
                left_sides.append(south_tile)
                left_sides.append(southwest_tile)
                left_sides.append(west_tile)
                coming_from = "south"
            else:
                raise ValueError(current_type, coming_from)

        elif current_type == "J":
            if coming_from == "north":
                left_sides.append(east_tile)
                left_sides.append(southeast_tile)
                left_sides.append(south_tile)
                right_sides.append(northwest_tile)
                coming_from = "east"
            elif coming_from == "west":
                left_sides.append(northwest_tile)
                right_sides.append(east_tile)
                right_sides.append(southeast_tile)
                right_sides.append(south_tile)
                coming_from = "south"

            else:
                raise ValueError(current_type, coming_from)

        for dtile in left_sides:
            if dtile and dtile.type == ".":
                dtile.type = "1"

        for dtile in right_sides:
            if dtile and dtile.type == ".":
                dtile.type = "2"


def calculate_solution(input_values: InputType) -> int:
    pipe_map = NetworkMap(input_values[0])

    remove_junk_tiles(pipe_map)

    # Mark all elements on the border or connected to another outsider as "O"
    iter_cover_outers(pipe_map)

    # Walk the pipe and categorize left and right
    traverse_and_categorize(pipe_map)

    # This is done for printing the beauty.
    for tile in pipe_map.tiles:
        if tile.type == ".":
            tile.type = "X"
        elif tile.type != "1" and tile.type != "2" and tile.position() not in pipe_map.network_map:
            tile.type = " "

    # Colorful print for inspection
    print(pipe_map)

    # Using that we saw that "2" is "inside" and all remaining "X"s are in a middle region.
    return sum(tile.type in ("X", "2") for tile in pipe_map.tiles)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
