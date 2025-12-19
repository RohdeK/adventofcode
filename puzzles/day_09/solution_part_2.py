import itertools

from puzzles.day_09.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Direction, Position


def area_of(t1: Position, t2: Position) -> int:
    return (abs((t1[0] - t2[0])) + 1) * (abs((t1[1] - t2[1])) + 1)


def is_inside(v: Position, t1: Position, t2: Position) -> bool:
    if (t1[0] < v[0] < t2[0] or t2[0] < v[0] < t1[0]) and (
        t1[1] < v[1] < t2[1] or t2[1] < v[1] < t1[1]
    ):
        return True

    return False


def to_direction(p1: Position, p2: Position) -> Direction:
    if p2[0] > p1[0]:
        return Direction.RIGHT
    elif p2[0] < p1[0]:
        return Direction.LEFT
    elif p2[1] > p1[1]:
        return Direction.DOWN
    elif p2[1] < p1[1]:
        return Direction.UP
    else:
        raise ValueError(p1, p2)


def left_right_corners(dir1: Direction, dir2: Direction) -> tuple[list[Position], list[Position]]:
    left_corners: dict[tuple[Direction, Direction], list[Position]] = {
        (Direction.LEFT, Direction.DOWN): [(1, 1)],
        (Direction.UP, Direction.LEFT): [(-1, 1)],
        (Direction.RIGHT, Direction.UP): [(-1, -1)],
        (Direction.DOWN, Direction.RIGHT): [(1, -1)],
        (Direction.LEFT, Direction.UP): [(1, 1), (-1, -1), (-1, 1)],
        (Direction.UP, Direction.RIGHT): [(-1, -1), (-1, 1), (1, -1)],
        (Direction.RIGHT, Direction.DOWN): [(1, 1), (-1, -1), (1, -1)],
        (Direction.DOWN, Direction.LEFT): [(1, 1), (-1, 1), (1, -1)],
    }

    right_corners: dict[tuple[Direction, Direction], list[Position]] = {
        (Direction.LEFT, Direction.DOWN): [(1, -1), (-1, 1), (-1, -1)],
        (Direction.UP, Direction.LEFT): [(1, -1), (-1, -1), (1, 1)],
        (Direction.RIGHT, Direction.UP): [(1, -1), (-1, 1), (1, 1)],
        (Direction.DOWN, Direction.RIGHT): [(-1, 1), (-1, -1), (1, 1)],
        (Direction.LEFT, Direction.UP): [(1, -1)],
        (Direction.UP, Direction.RIGHT): [(1, 1)],
        (Direction.RIGHT, Direction.DOWN): [(-1, 1)],
        (Direction.DOWN, Direction.LEFT): [(-1, -1)],
    }

    return left_corners[(dir1, dir2)], right_corners[(dir1, dir2)]


def is_in(v: Position, t1: Position, t2: Position) -> bool:
    if (t1[0] <= v[0] <= t2[0] or t2[0] <= v[0] <= t1[0]) and (
        t1[1] <= v[1] <= t2[1] or t2[1] <= v[1] <= t1[1]
    ):
        return True

    return False


def calculate_solution(input_values: InputType) -> int:
    max_area_left = 0
    max_area_right = 0
    max_area_unknown = 0

    wrapped = [*input_values, input_values[0], input_values[1]]

    left_corners = []
    right_corners = []

    something_was_inside = 0
    something_was_insideout = 0
    something_traversed = 0

    for i in range(len(input_values)):
        t1, t2, t3 = wrapped[i], wrapped[i + 1], wrapped[i + 2]
        dir1 = to_direction(t1, t2)
        dir2 = to_direction(t2, t3)

        lefts, rights = left_right_corners(dir1, dir2)

        left_corners.extend([(t2[0] + x, t2[1] + y) for x, y in lefts])
        right_corners.extend([(t2[0] + x, t2[1] + y) for x, y in rights])

    left_corners_inner = []
    right_corners_inner = []

    for lc in left_corners:
        is_inner = True

        for i in range(len(input_values)):
            t1, t2 = wrapped[i], wrapped[i + 1]

            if t1[0] == t2[0] == lc[0]:
                if t1[1] <= lc[1] <= t2[1] or t2[1] <= lc[1] <= t1[1]:
                    is_inner = False
                    break
            elif t1[1] == t2[1] == lc[1]:
                if t1[0] <= lc[0] <= t2[0] or t2[0] <= lc[0] <= t1[0]:
                    is_inner = False
                    break

        if is_inner:
            left_corners_inner.append(lc)

    for rc in right_corners:
        is_inner = True

        for i in range(len(input_values)):
            t1, t2 = wrapped[i], wrapped[i + 1]

            if t1[0] == t2[0] == rc[0]:
                if t1[1] <= rc[1] <= t2[1] or t2[1] <= rc[1] <= t1[1]:
                    is_inner = False
                    break
            elif t1[1] == t2[1] == rc[1]:
                if t1[0] <= rc[0] <= t2[0] or t2[0] <= rc[0] <= t1[0]:
                    is_inner = False
                    break

        if is_inner:
            right_corners_inner.append(rc)

    left_is_out = min(x1 + x2 for x1, x2 in left_corners) < min(x1 + x2 for x1, x2 in right_corners)

    for t0, t1 in itertools.combinations(input_values, 2):
        potential_area = area_of(t0, t1)

        is_line = t0[0] == t1[0] or t0[1] == t1[1]

        if is_line:
            if potential_area > max_area_left:
                max_area_left = potential_area
            if potential_area > max_area_right:
                max_area_right = potential_area
            continue

        no_corner_inside = True

        for t2 in input_values:
            if is_inside(t2, t0, t1):
                no_corner_inside = False
                break

        if not no_corner_inside:
            something_was_inside += 1
            continue

        no_traverse_inside = True

        for i in range(len(input_values)):
            l1, l2 = wrapped[i], wrapped[i + 1]

            if l1[0] == l2[0]:
                if t0[0] < l1[0] < t1[0] or t1[0] < l1[0] < t0[0]:
                    if (l1[1] < min(t0[1], t1[1]) and l2[1] > max(t0[1], t1[1])) or (l2[1] < min(t0[1], t1[1]) and l1[1] > max(t0[1], t1[1])):
                        no_traverse_inside = False
                        break
            elif l1[1] == l2[1]:
                if t0[1] < l1[1] < t1[1] or t1[1] < l1[1] < t0[1]:
                    if (l1[0] < min(t0[0], t1[0]) and l2[0] > max(t0[0], t1[0])) or (l2[0] < min(t0[0], t1[0]) and l1[0] > max(t0[0], t1[0])):
                        no_traverse_inside = False
                        break

        if not no_traverse_inside:
            something_traversed += 1
            continue

        is_left = False
        is_right = False

        for t2 in left_corners_inner:
            if is_in(t2, t0, t1):
                is_left = True
                break

        for t2 in right_corners_inner:
            if is_in(t2, t0, t1):
                is_right = True
                break

        if is_left and is_right:
            something_was_insideout += 1
            continue
        elif is_left:
            if potential_area > max_area_left:
                max_area_left = potential_area
        elif is_right:
            if potential_area > max_area_right:
                max_area_right = potential_area
        else:
            print(t0, t1)
            if potential_area > max_area_unknown:
                max_area_unknown = potential_area

    print("left", max_area_left)
    print("right", max_area_right)
    print("unk", max_area_unknown)

    print("inside", something_was_inside)
    print("traverse", something_traversed)
    print("insideout", something_was_insideout)

    if left_is_out:
        return max_area_right
    else:
        return max_area_left


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
