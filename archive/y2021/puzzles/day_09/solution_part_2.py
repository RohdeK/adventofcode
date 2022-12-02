from functools import reduce
from typing import Generic, List, Tuple, TypeVar

from archive.y2021.puzzles.day_09.input_part_1 import get_input

T = TypeVar("T")


class EquivalenceClassBuilder(Generic[T]):
    def __init__(self):
        self.classes: List[List[T]] = []

    def set_equal(self, val1: T, val2: T) -> None:
        class_of_1 = next((cls for cls in self.classes if val1 in cls), None)
        class_of_2 = next((cls for cls in self.classes if val2 in cls), None)

        if class_of_1 and not class_of_2:
            val2 not in class_of_1 and class_of_1.append(val2)
        elif class_of_2 and not class_of_1:
            val1 not in class_of_2 and class_of_2.append(val1)
        elif not class_of_1 and not class_of_2:
            self.classes.append([val1, val2])
        elif class_of_1 is class_of_2:
            pass
        else:
            joined = list(set(class_of_1 + class_of_2))
            self.classes.remove(class_of_1)
            self.classes.remove(class_of_2)
            self.classes.append(joined)


def find_basins(input_values: List[List[int]]) -> List[List[Tuple[int, int]]]:
    basins = EquivalenceClassBuilder[Tuple[int, int]]()

    for i, row in enumerate(input_values):
        for j, val in enumerate(row):

            if val == 9:
                continue

            if j > 0 and row[j - 1] <= val:
                # Left value is smaller
                basins.set_equal((i, j), (i, j - 1))
            if j < len(row) - 1 and row[j + 1] <= val:
                # Right value is smaller
                basins.set_equal((i, j), (i, j + 1))
            if i > 0 and input_values[i - 1][j] <= val:
                # Top value is smaller
                basins.set_equal((i, j), (i - 1, j))
            if i < len(input_values) - 1 and input_values[i + 1][j] <= val:
                # Bottom value is smaller
                basins.set_equal((i, j), (i + 1, j))

    return basins.classes


def find_basin_sizes(input_values: List[List[int]]) -> List[int]:
    return [len(basin) for basin in find_basins(input_values)]


def basin_size_proof_numer(input_values: List[List[int]]) -> int:
    basin_sizes = find_basin_sizes(input_values)

    top_three = sorted(basin_sizes, reverse=True)[0:3]

    return reduce(lambda x, y: x * y, top_three)


if __name__ == "__main__":
    print(basin_size_proof_numer(get_input()))
