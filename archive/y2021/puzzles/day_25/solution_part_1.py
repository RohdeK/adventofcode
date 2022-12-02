from typing import List, Tuple

from archive.y2021.puzzles.day_25.input_part_1 import get_input


def calculate_solution(input_values: List[str]) -> int:
    def pretty_print(fild):
        raw = [["#" for _ in range(x_dim)] for _ in range(y_dim)]

        for (x, y), val in fild.items():
            raw[y][x] = val

        joined = "\n" + "\n".join(["".join(row) for row in raw])
        print(joined)

    x_dim = len(input_values[0])
    y_dim = len(input_values)

    field = {(i, j): val for (j, row) in enumerate(input_values) for (i, val) in enumerate(row)}

    zero_indices = [index for index, val in field.items() if val == "."]

    any_moved = True
    steps = 0

    # pretty_print(field)

    while any_moved:
        any_moved = False
        iter_zero_indices: List[Tuple[int, int]] = []
        iter_field = field.copy()

        steps += 1

        for (x, y) in zero_indices:

            look_index = (x if x > 0 else x_dim) - 1, y

            if field[look_index] == ">":
                iter_zero_indices.append(look_index)
                iter_field[look_index] = "."
                iter_field[(x, y)] = ">"
                any_moved = True
            else:
                iter_zero_indices.append((x, y))

        zero_indices = []
        field = iter_field
        iter_field = field.copy()

        for (x, y) in iter_zero_indices:

            look_index = x, (y if y > 0 else y_dim) - 1

            if field[look_index] == "v":
                zero_indices.append(look_index)
                iter_field[look_index] = "."
                iter_field[(x, y)] = "v"
                any_moved = True
            else:
                zero_indices.append((x, y))

        field = iter_field

        # pretty_print(field)

    return steps


if __name__ == "__main__":
    print(calculate_solution(get_input()))
