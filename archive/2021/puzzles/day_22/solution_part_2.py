from typing import List

from puzzles.day_22.input_part_1 import get_input
from puzzles.day_22.solution_part_1 import Cube, CubeSet


def calculate_solution(input_values: List[str]) -> int:
    cube_set = CubeSet()

    for rep in input_values:
        cube = Cube.from_rep(rep)

        if cube:
            cube_set.merge(cube)

    return cube_set.volume()


if __name__ == "__main__":
    print(calculate_solution(get_input()))
