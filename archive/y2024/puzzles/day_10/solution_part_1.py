from typing import Iterable

from archive.y2024.puzzles.day_10.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Location, PlanarMap


class TrailMap(PlanarMap):
    def heads(self) -> Iterable[Location]:
        return self.tiles_by_type["0"]

    def score(self, head: Location) -> tuple[int, int]:
        assert head.type == "0"

        trail_endings_found = set()
        trails_found = 0
        positions_to_check = [head]

        while positions_to_check:
            p = positions_to_check.pop(0)
            curr_height = int(p.type)

            for next_p in self.surrounding(p, including_diagonals=False):
                if next_p.type == ".":
                    continue

                next_height = int(next_p.type)
                if next_height != curr_height + 1:
                    continue

                if next_height == 9:
                    trail_endings_found.add(next_p.position())
                    trails_found += 1
                else:
                    positions_to_check.append(next_p)

        return len(trail_endings_found), trails_found


def calculate_solution(input_values: InputType) -> int:
    trails = TrailMap(input_values)

    checksum = 0

    for thead in trails.heads():
        checksum += trails.score(thead)[0]

    return checksum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
