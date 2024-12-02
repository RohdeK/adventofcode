from typing import List, Tuple

from puzzles.day_18.load_inputs import InputType, input_reader
from utils.common_structures.planar_map import Location


def build_corners_from_instructions(input_values: List[Tuple[str, int]]) -> List[Location]:
    locations = []
    cl = (0, 0)
    for direction, distance in input_values:
        if direction == "D":
            cl = cl[0] + distance, cl[1]
        elif direction == "U":
            cl = cl[0] - distance, cl[1]
        elif direction == "L":
            cl = cl[0], cl[1] - distance
        elif direction == "R":
            cl = cl[0], cl[1] + distance

        locations.append(Location(row=cl[0], col=cl[1], type=direction))

    min_row = min(loc.row for loc in locations)
    min_col = min(loc.col for loc in locations)

    for loc in locations:
        loc.row += 1 - min_row
        loc.col += 1 - min_col

    return locations


def corner_segment(locators: List[Tuple[str, int]]) -> int:
    corners = build_corners_from_instructions(locators)
    solved_area = 0

    while True:
        if len(corners) == 4:
            row_dist_1, col_dist_1 = abs(corners[0].row - corners[1].row), abs(corners[0].col - corners[1].col)
            row_dist_2, col_dist_2 = abs(corners[1].row - corners[2].row), abs(corners[1].col - corners[2].col)
            solved_area += (row_dist_1 + 1) * (col_dist_2 + 1) if row_dist_2 == 0 else (row_dist_2 + 1) * (col_dist_1 + 1)
            break

        type_seq = corners[-1].type + corners[0].type + corners[1].type

        if type_seq in ("URD", "RDL", "DLU", "LUR"):
            prev_prev_corner = corners[-2]
            previous_corner = corners[-1]
            current_corner = corners[0]
            next_corner = corners[1]

            if current_corner.type == "R":
                row_shift = min(prev_prev_corner.row, next_corner.row) - current_corner.row

                # if any corners in range: continue
                if any(
                    previous_corner.col < loc.col < current_corner.col and
                    current_corner.row < loc.row <= current_corner.row + row_shift
                    for loc in corners
                ):
                    corners.append(corners.pop(0))
                    continue

                previous_corner.row += row_shift
                current_corner.row += row_shift
                solved_area += row_shift * (current_corner.col - previous_corner.col + 1)

            elif current_corner.type == "L":
                row_shift = current_corner.row - max(prev_prev_corner.row, next_corner.row)

                # if any corners in range: continue
                if any(
                    current_corner.col < loc.col < previous_corner.col and
                    current_corner.row - row_shift <= loc.row < current_corner.row
                    for loc in corners
                ):
                    corners.append(corners.pop(0))
                    continue

                previous_corner.row -= row_shift
                current_corner.row -= row_shift
                solved_area += row_shift * (previous_corner.col - current_corner.col + 1)

            elif current_corner.type == "U":
                col_shift = min(prev_prev_corner.col, next_corner.col) - current_corner.col

                # if any corners in range: continue
                if any(
                    current_corner.row < loc.row < previous_corner.row and
                    current_corner.col < loc.col <= current_corner.col + col_shift
                    for loc in corners
                ):
                    corners.append(corners.pop(0))
                    continue

                previous_corner.col += col_shift
                current_corner.col += col_shift
                solved_area += col_shift * (previous_corner.row - current_corner.row + 1)

            elif current_corner.type == "D":
                col_shift = current_corner.col - max(prev_prev_corner.col, next_corner.col)

                # if any corners in range: continue
                if any(
                    previous_corner.row < loc.row < current_corner.row and
                    current_corner.col - col_shift <= loc.col < current_corner.col
                    for loc in corners
                ):
                    corners.append(corners.pop(0))
                    continue

                previous_corner.col -= col_shift
                current_corner.col -= col_shift
                solved_area += col_shift * (current_corner.row - previous_corner.row + 1)

            # consolidate
            anychange = True
            while anychange:
                anychange = False
                t_minus_1 = corners[-1]
                t_minus_2 = corners[-2]
                for t_minus_0 in tuple(corners):
                    if t_minus_0.row == t_minus_1.row == t_minus_2.row:
                        corners.remove(t_minus_1)
                        excess_area = (abs(t_minus_1.col - t_minus_0.col) + abs(t_minus_2.col - t_minus_1.col) - abs(t_minus_0.col - t_minus_2.col)) // 2
                        solved_area += excess_area

                        if t_minus_0.col < t_minus_2.col:
                            t_minus_0.type = "L"
                        else:
                            t_minus_0.type = "R"

                        anychange = True
                        break
                    elif t_minus_0.col == t_minus_1.col == t_minus_2.col:
                        corners.remove(t_minus_1)
                        excess_area = (abs(t_minus_1.row - t_minus_0.row) + abs(t_minus_2.row - t_minus_1.row) - abs(t_minus_0.row - t_minus_2.row)) // 2
                        solved_area += excess_area

                        if t_minus_0.row < t_minus_2.row:
                            t_minus_0.type = "U"
                        else:
                            t_minus_0.type = "D"

                        anychange = True
                        break
                    else:
                        t_minus_2 = t_minus_1
                        t_minus_1 = t_minus_0

        else:
            # Rotate input values
            corners.append(corners.pop(0))

    return solved_area


def calculate_solution(input_values: InputType) -> int:
    corrected_distances = []

    for _, _, code in input_values:
        distance_code = code[2:7]
        direction = {"0": "R", "1": "D", "2": "L", "3": "U"}[code[7]]
        distance = int(distance_code, 16)

        corrected_distances.append((direction, distance))

    return corner_segment(corrected_distances)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
