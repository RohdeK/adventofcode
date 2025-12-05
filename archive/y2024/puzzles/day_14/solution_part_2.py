from archive.y2024.puzzles.day_14.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Location, PlanarMap, Position


def is_on_tree(pos: Position, max_sides: Position) -> bool:
    middle_x = (max_sides[0] - 1) // 2

    if pos == (middle_x, max_sides[1] - 1):
        return True

    if abs(pos[0] - middle_x) == pos[1]:
        return True

    if pos in [
        (5, 0),
        (4, 1),
        (6, 1),
        (3, 2),
        (7, 2),
        (2, 3),
        (8, 3),
        (1, 4),
        (9, 4),
        (0, 5),
        (10, 5),
        (5, 6),
    ]:
        raise RuntimeError(f"Fucked up {pos}")

    return False


def pass_second(pos: Position, vec: Position, max_sides: Position) -> Position:
    return (pos[0] + vec[0]) % max_sides[0], (pos[1] + vec[1]) % max_sides[1]


def pass_second_all(values: InputType, max_sides: Position) -> InputType:
    new_vals = []
    for (p, v) in values:
        new_p = pass_second(p, v, max_sides)
        new_vals.append((new_p, v))

    return new_vals


def viz(input_values: InputType) -> None:
    print("\n")
    print(PlanarMap([Location(p[1], p[0], "X") for p, v in input_values]))


def is_formation(input_values: InputType, target_values: list[Position]) -> bool:
    return target_values == sorted([p for p, v in input_values])


def make_tree(max_sides: Position) -> list[Position]:
    middle_x = (max_sides[0] - 1) // 2
    positions = [(middle_x, 0), (middle_x, max_sides[1] - 1)]

    for i in range(1, max_sides[1] - 1):
        positions.append((middle_x - i, i))
        positions.append((middle_x + i, i))

    return sorted(positions)


def calculate_solution(input_values: InputType, max_sides: Position) -> int:
    viz(input_values)
    model_tree = make_tree(max_sides)

    for i in range(max_sides[0] * max_sides[1]):
        if is_formation(input_values, model_tree):
            viz(input_values)
            return i
        input_values = pass_second_all(input_values, max_sides)
        print(i)
        viz(input_values)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input, (101, 103)))
