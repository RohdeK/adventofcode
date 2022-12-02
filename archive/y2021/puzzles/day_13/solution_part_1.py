from typing import List, Tuple

from archive.y2021.puzzles.day_13.input_part_1 import get_input


def fold_paper_horizontally(input_values: List[Tuple[int, int]], fold_line: int) -> List[Tuple[int, int]]:
    out_vals: List[Tuple[int, int]] = []

    for val in input_values:
        if val[1] < fold_line:
            out_vals.append(val)

        elif val[1] > fold_line:
            out_vals.append((val[0], 2 * fold_line - val[1]))

        else:
            raise ValueError(f"Point {val} found on fold line {fold_line}.")

    return list(set(out_vals))


def fold_paper_vertically(input_values: List[Tuple[int, int]], fold_line: int) -> List[Tuple[int, int]]:
    out_vals: List[Tuple[int, int]] = []

    for val in input_values:
        if val[0] < fold_line:
            out_vals.append(val)

        elif val[0] > fold_line:
            out_vals.append((2 * fold_line - val[0], val[1]))

        else:
            raise ValueError(f"Point {val} found on fold line {fold_line}.")

    return list(set(out_vals))


def fold_dotted_paper(input_values: List[Tuple[int, int]], fold_instructions: Tuple[int, int]) -> List[Tuple[int, int]]:
    if fold_instructions[0] == 0:
        return fold_paper_horizontally(input_values, fold_instructions[1])
    elif fold_instructions[1] == 0:
        return fold_paper_vertically(input_values, fold_instructions[0])
    else:
        raise ValueError(f"Illegal fold instruction: {fold_instructions}")


if __name__ == "__main__":
    dots, instructions = get_input()

    folded = fold_dotted_paper(dots, instructions[0])

    print(len(folded))
