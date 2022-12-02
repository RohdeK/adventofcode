from typing import Iterator, List, Tuple

from puzzles.day_09.input_part_1 import get_input


def deepest_spots_risk(input_values: List[List[int]]) -> int:
    deepest_spots = find_deepest_spots(input_values)

    return sum(input_values[i][j] + 1 for i, j in deepest_spots)


def find_deepest_spots(input_values: List[List[int]]) -> Iterator[Tuple[int, int]]:
    for i, row in enumerate(input_values):
        for j, val in enumerate(row):

            if j > 0 and row[j - 1] <= val:
                # Left value is smaller
                continue
            elif j < len(row) - 1 and row[j + 1] <= val:
                # Right value is smaller
                continue
            elif i > 0 and input_values[i - 1][j] <= val:
                # Top value is smaller
                continue
            elif i < len(input_values) - 1 and input_values[i + 1][j] <= val:
                # Bottom value is smaller
                continue
            else:
                yield i, j


if __name__ == "__main__":
    print(deepest_spots_risk(get_input()))
