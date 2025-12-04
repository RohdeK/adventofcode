from typing import List

from archive.y2023.puzzles.day_10.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Location, PlanarMap


def get_any_connecting(pipe_map: PlanarMap, from_tile: Location) -> Location:
    if to_top := pipe_map.get_location_north(from_tile):
        if to_top.type in ("|", "7", "F"):
            return to_top

    if to_bottom := pipe_map.get_location_south(from_tile):
        if to_bottom.type in ("|", "J", "L"):
            return to_bottom

    if to_left := pipe_map.get_location_west(from_tile):
        if to_left.type in ("-", "F", "L"):
            return to_left

    if to_right := pipe_map.get_location_east(from_tile):
        if to_right.type in ("-", "J", "7"):
            return to_right

    raise ValueError("No connecting found to", from_tile)


def get_connecting(pipe_map: PlanarMap, from_tile: Location, not_to: Location) -> Location:
    to_top = pipe_map.get_location_north(from_tile)
    to_bottom = pipe_map.get_location_south(from_tile)
    to_left = pipe_map.get_location_west(from_tile)
    to_right = pipe_map.get_location_east(from_tile)

    if from_tile.type == "-":
        return to_left if to_left != not_to else to_right

    elif from_tile.type == "|":
        return to_top if to_top != not_to else to_bottom

    elif from_tile.type == "7":
        return to_left if to_left != not_to else to_bottom

    elif from_tile.type == "F":
        return to_right if to_right != not_to else to_bottom

    elif from_tile.type == "J":
        return to_left if to_left != not_to else to_top

    elif from_tile.type == "L":
        return to_right if to_right != not_to else to_top

    raise ValueError("Connecting not found", from_tile, "not", not_to)


def build_network(pipe_map: PlanarMap) -> List[Location]:
    start_tile = next(t for t in pipe_map.tiles if t.type == "S")
    tiles_covered = [start_tile]

    next_tile = get_any_connecting(pipe_map, start_tile)

    while next_tile != start_tile:
        tiles_covered.append(next_tile)
        next_tile = get_connecting(pipe_map, next_tile, tiles_covered[-2])

    return tiles_covered


def calculate_solution(input_values: InputType) -> int:
    pipe_map = PlanarMap(input_values[0])

    pipe_network = build_network(pipe_map)

    return len(pipe_network) // 2


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
