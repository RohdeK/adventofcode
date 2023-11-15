from typing import Iterator, Set

from archive.y2022.puzzles.day_18.load_inputs import Cubelet, input_reader, InputType
from archive.y2022.puzzles.day_18.solution_part_1 import calculate_solution as get_facets_of


class SteamEnclosure:
    def __init__(self, cubes: InputType):
        self.lava_cubes = [tuple(c) for c in cubes]
        self.x_min, self.y_min, self.z_min = cubes[0]
        self.x_max, self.y_max, self.z_max = cubes[0]

        self.steam_cubes: Set[Cubelet] = set()
        self.current_steam_sources: Set[Cubelet] = set()

        self.detect_outmost()

    def detect_outmost(self) -> None:
        for cube_x, cube_y, cube_z in self.lava_cubes:
            if cube_x < self.x_min:
                self.x_min = cube_x
            if cube_x > self.x_max:
                self.x_max = cube_x
            if cube_y < self.y_min:
                self.y_min = cube_y
            if cube_y > self.y_max:
                self.y_max = cube_y
            if cube_z < self.z_min:
                self.z_min = cube_z
            if cube_z > self.z_max:
                self.z_max = cube_z

        self.x_min -= 1
        self.x_max += 1
        self.y_min -= 1
        self.y_max += 1
        self.z_min -= 1
        self.z_max += 1

    def test_volume(self):
        return (self.x_max - self.x_min + 1) * (self.y_max - self.y_min + 1) * (1 + self.z_max - self.z_min)

    def initialize_steam(self) -> None:
        for x in range(self.x_min, self.x_max + 1):
            for y in range(self.y_min, self.y_max + 1):
                self.steam_cubes.add((x, y, self.z_min))
                self.steam_cubes.add((x, y, self.z_max))

            for z in range(self.z_min, self.z_max):
                self.steam_cubes.add((x, self.y_min, z))
                self.steam_cubes.add((x, self.y_max, z))

        for y in range(self.y_min, self.y_max):
            for z in range(self.z_min, self.z_max):
                self.steam_cubes.add((self.x_min, y, z))
                self.steam_cubes.add((self.x_max, y, z))

        self.current_steam_sources = self.steam_cubes

    def jitter_cube(self, cube: Cubelet) -> Iterator[Cubelet]:
        cube_x, cube_y, cube_z = cube

        if cube_x > self.x_min:
            yield cube_x - 1, cube_y, cube_z
        if cube_x < self.x_max:
            yield cube_x + 1, cube_y, cube_z
        if cube_y > self.y_min:
            yield cube_x, cube_y - 1, cube_z
        if cube_y < self.y_max:
            yield cube_x, cube_y + 1, cube_z
        if cube_z > self.z_min:
            yield cube_x, cube_y, cube_z - 1
        if cube_z < self.z_max:
            yield cube_x, cube_y, cube_z + 1

    def propagate_steam(self) -> None:
        if not self.steam_cubes:
            self.initialize_steam()

        next_steam_cubes: Set[Cubelet] = set()

        for cube in self.current_steam_sources:
            for next_cube in self.jitter_cube(cube):
                if next_cube in self.lava_cubes:
                    continue
                if next_cube in next_steam_cubes:
                    continue
                if next_cube in self.steam_cubes:
                    continue
                next_steam_cubes.add(next_cube)

        for cube in next_steam_cubes:
            self.steam_cubes.add(cube)

        self.current_steam_sources = next_steam_cubes

    def flow_steam(self) -> None:
        self.initialize_steam()

        while self.current_steam_sources:
            self.propagate_steam()

    def num_outer_steam_facets(self) -> int:
        total_outer_facets = 0
        total_outer_facets += 2 * (self.x_max - self.x_min + 1) * (self.y_max - self.y_min + 1)
        total_outer_facets += 2 * (self.x_max - self.x_min + 1) * (self.z_max - self.z_min + 1)
        total_outer_facets += 2 * (self.z_max - self.z_min + 1) * (self.y_max - self.y_min + 1)
        return total_outer_facets


def calculate_solution(input_values: InputType) -> int:
    se = SteamEnclosure(input_values)

    se.flow_steam()

    return get_facets_of(se.steam_cubes) - se.num_outer_steam_facets()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
