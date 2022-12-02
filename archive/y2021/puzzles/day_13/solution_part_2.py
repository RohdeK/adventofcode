from typing import List, Tuple

from archive.y2021.puzzles.day_13.input_part_1 import get_input
from archive.y2021.puzzles.day_13.solution_part_1 import fold_dotted_paper


def display_dots(input_values: List[Tuple[int, int]]) -> str:
    grid_size = max((val[0]) for val in input_values) + 1, max((val[1]) for val in input_values) + 1

    display_field = [[" "] * grid_size[0] for _ in range(grid_size[1])]

    for dot in input_values:
        if dot[0] == 2 and dot[1] == 2:
            raise ValueError
        display_field[dot[1]][dot[0]] = "x"

    return "\n" + "\n".join("".join(row) for row in display_field) + "\n"


def fold_dotted_paper_full(
    input_dots: List[Tuple[int, int]], input_folds: List[Tuple[int, int]]
) -> List[Tuple[int, int]]:
    for instruction in input_folds:
        input_dots = fold_dotted_paper(input_dots, instruction)

    return input_dots


if __name__ == "__main__":
    dots, instructions = get_input()

    folded = fold_dotted_paper_full(dots, instructions)

    print(display_dots(folded))
