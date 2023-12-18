from typing import List, Tuple

from puzzles.day_18.load_inputs import input_reader, InputType
from puzzles.day_18.solution_part_1 import build_locations_from_instructions
from utils.common_structures.planar_map import Located, Location, PlanarMap


def print_map(current_locator: List[Tuple[str, int]]) -> PlanarMap:
    locations = build_locations_from_instructions([[r, str(c), "nice"] for r, c in current_locator])
    trench_map = PlanarMap(locations)
    print(trench_map)
    return trench_map


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
    # original_map = print_from_corners(corners)

    def add_solved_square(*cs: Located) -> None:
        return None
        # nonlocal original_map

        min_row = min(c.row for c in cs)
        max_row = max(c.row for c in cs)
        min_col = min(c.col for c in cs)
        max_col = max(c.col for c in cs)

        for row in range(min_row, max_row + 1):
            for col in range(min_col, max_col + 1):
                if original_map.tiles_by_loc[(row, col)].type == ".":
                    original_map.tiles_by_loc[(row, col)].type = "#"

    while True:
        if len(corners) == 4:
            row_dist_1, col_dist_1 = abs(corners[0].row - corners[1].row), abs(corners[0].col - corners[1].col)
            row_dist_2, col_dist_2 = abs(corners[1].row - corners[2].row), abs(corners[1].col - corners[2].col)
            solved_area += (row_dist_1 + 1) * (col_dist_2 + 1) if row_dist_2 == 0 else (row_dist_2 + 1) * (col_dist_1 + 1)

            add_solved_square(*corners)
            break

        type_seq = corners[-1].type + corners[0].type + corners[1].type

        if type_seq in ("URD", "RDL", "DLU", "LUR"):
            # print(len(corners))
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

                add_solved_square(
                    Located(row=previous_corner.row - 1, col=previous_corner.col),
                    Located(row=previous_corner.row - row_shift, col=previous_corner.col),
                    Located(row=current_corner.row - row_shift, col=current_corner.col),
                    Located(row=current_corner.row - 1, col=current_corner.col),
                )
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
                add_solved_square(
                    Located(row=previous_corner.row + 1, col=previous_corner.col),
                    Located(row=previous_corner.row + row_shift, col=previous_corner.col),
                    Located(row=current_corner.row + row_shift, col=current_corner.col),
                    Located(row=current_corner.row + 1, col=current_corner.col),
                )
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

                add_solved_square(
                    Located(row=previous_corner.row, col=previous_corner.col - 1),
                    Located(row=previous_corner.row, col=previous_corner.col - col_shift),
                    Located(row=current_corner.row, col=current_corner.col - col_shift),
                    Located(row=current_corner.row, col=current_corner.col - 1),
                )
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

                add_solved_square(
                    Located(row=previous_corner.row, col=previous_corner.col + 1),
                    Located(row=previous_corner.row, col=previous_corner.col + col_shift),
                    Located(row=current_corner.row, col=current_corner.col + col_shift),
                    Located(row=current_corner.row, col=current_corner.col + 1),
                )

            # if previous_corner.position() == prev_prev_corner.position():
            #     corners.pop(-1)
            #     if prev_prev_corner.type + current_corner.type in ("LR", "RL", "UD", "DU"):
            #         corners.pop(-1)
            #         solved_area += abs(current_corner.col - prev_prev_corner.col) + abs(current_corner.row - prev_prev_corner.row)
            # elif current_corner.position() == next_corner.position():
            #     corners.pop(0)
            #     if previous_corner.type + next_corner.type in ("LR", "RL", "UD", "DU"):
            #         corners.pop(-1)
            #         solved_area += abs(next_corner.col - previous_corner.col) + abs(next_corner.row - previous_corner.row)
            #
            print(len(corners))

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

            # if len(corners) < 200:
            #     print_from_corners(corners)
            #     print("NIce")
        else:
            # Rotate input values
            corners.append(corners.pop(0))

    return solved_area


def print_from_corners(c: List[Location]) -> PlanarMap:
    directions = []
    prev_corn = c[-1]
    for corn in c:
        row_gap, col_gap = corn.row - prev_corn.row, corn.col - prev_corn.col
        if corn.type == "R":
            directions.append(("R", col_gap))
        elif corn.type == "D":
            directions.append(("D", row_gap))
        elif corn.type == "U":
            directions.append(("U", -row_gap))
        elif corn.type == "L":
            directions.append(("L", -col_gap))
        prev_corn = corn

    return print_map(directions)


def iteratively_segment(input_values: List[Tuple[str, int]]) -> int:
    solved_area = 0
    reorder_counter = 0

    while True:
        if len(input_values) == 4:
            assert "".join(sorted(i[0] for i in input_values)) == "DLRU"
            assert input_values[0][1] == input_values[2][1]
            assert input_values[1][1] == input_values[3][1]
            solved_area += (input_values[0][1] + 1) * (input_values[1][1] + 1)
            break

        type_seq = input_values[-1][0] + input_values[0][0] + input_values[1][0]

        # if input_values[-2][0] != input_values[2][0] and reorder_counter < len(input_values):
        #     # Rotate input values to not deal with accidental fuckups
        #     input_values.append(input_values.pop(0))
        #     reorder_counter += 1

        if type_seq in ("URD", "RDL", "DLU", "LUR", "ULD", "RUL", "DRU",  "LDR"):
            reorder_counter = 0
            print(len(input_values))
            current_locator = [(r, str(c)) for r, c in input_values]
            if len(input_values) <= 480:
            # if input_values[0][1] < 0:
                print_map(current_locator)
            previous_segment = input_values.pop(-1)
            segment = input_values.pop(0)
            next_segment = input_values.pop(0)

            cut_len = min(previous_segment[1], next_segment[1])
            cut_area = [(segment[1] + 1) * cut_len]

            if previous_segment[1] == cut_len:
                prev_prev_segment = input_values.pop(-1)
                converge_type_seq = prev_prev_segment[0] + segment[0]
                if converge_type_seq in ("RR", "LL", "DD", "UU"):
                    # Lengthen after cut
                    input_values.append((prev_prev_segment[0], prev_prev_segment[1] + segment[1]))
                elif converge_type_seq in ("RL", "LR", "DU", "UD"):
                    # Shorten after cut and override direction
                    # print("Cut line", prev_prev_segment[1])
                    cut_area.append(prev_prev_segment[1])
                    if segment[1] - prev_prev_segment[1] < 0:
                        # overlap
                        input_values.append((prev_prev_segment[0], prev_prev_segment[1] - segment[1]))
                    else:
                        input_values.append((segment[0], segment[1] - prev_prev_segment[1]))
            else:
                input_values.append((previous_segment[0], previous_segment[1] - cut_len))

            if next_segment[1] == cut_len:
                next_next_segment = input_values.pop(0)
                converge_type_seq = next_next_segment[0] + segment[0]
                if converge_type_seq in ("RR", "LL", "DD", "UU"):
                    # Lengthen after cut
                    input_values.insert(0, (next_next_segment[0], next_next_segment[1] + segment[1]))
                elif converge_type_seq in ("RL", "LR", "DU", "UD"):
                    # Shorten after cut and override direction
                    cut_area.append(next_next_segment[1])
                    if segment[1] - next_next_segment[1] < 0:
                        # overlap
                        input_values.insert(0, (next_next_segment[0], next_next_segment[1] - segment[1]))
                    else:
                        input_values.insert(0, (segment[0], segment[1] - next_next_segment[1]))

                if next_segment[1] == previous_segment[1]:
                    # Case both have been cut to length: merge ends
                    first_segment = input_values.pop(0)
                    last_segment = input_values.pop(-1)
                    if first_segment[0] == last_segment[0]:
                        # same direction, segment was covered twice.
                        input_values.append((first_segment[0], first_segment[1] + last_segment[1] - segment[1]))
                    else:
                        print("here")

            else:
                input_values.insert(0, (next_segment[0], next_segment[1] - cut_len))

            if type_seq in ("ULD", "RUL", "DRU",  "LDR"):
                cut_area = -sum(cut_area)
            else:
                cut_area = sum(cut_area)
            solved_area += cut_area
            # print(cut_area, prev_prev_segment if previous_segment[1] == cut_len else None, previous_segment, segment, next_segment, next_next_segment if next_segment[1] == cut_len else None)

            print(cut_area)
            debug_locator = [previous_segment, segment, next_segment]
            if next_segment[1] == cut_len:
                debug_locator.append(next_next_segment)
            if previous_segment[1] == cut_len:
                debug_locator.insert(0, prev_prev_segment)
            print_map(debug_locator)

        else:
            # Rotate input values
            input_values.append(input_values.pop(0))

    return solved_area


def calculate_solution(input_values: InputType) -> int:
    print("\n")

    # return corner_segment([(direction, int(distance)) for direction, distance, _ in input_values])

    # return iteratively_segment([(direction, int(distance)) for direction, distance, _ in input_values])

    corrected_distances = []

    for _, _, code in input_values:
        distance_code = code[2:7]
        direction = {"0": "R", "1": "D", "2": "L", "3": "U"}[code[7]]
        distance = int(distance_code, 16)

        corrected_distances.append((direction, distance))
    return corner_segment(corrected_distances)
    return iteratively_segment(corrected_distances)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
