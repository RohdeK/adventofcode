from puzzles.day_14.load_inputs import input_reader, InputType
from puzzles.day_14.solution_part_1 import BoulderMap
from utils.common_structures.planar_map import parse_map_lines


def calculate_solution(input_values: InputType, max_count: int) -> int:
    print("\n")
    bmap = BoulderMap(input_values[0])

    roll_order = ["north", "west", "south", "east"]

    seen_confs = []

    for i in range(max_count):
        for r in roll_order:
            bmap.roll(r)

        snapshot = repr(bmap)

        if snapshot in seen_confs:
            seen_at = seen_confs.index(snapshot)
            periodicity = i - seen_at
            final_in_period = (max_count - i - 1) % periodicity
            final_repr = seen_confs[seen_at + final_in_period]

            return BoulderMap(parse_map_lines(final_repr)).sum_weights()

        else:
            seen_confs.append(snapshot)

    return bmap.sum_weights()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input, 1_000_000_000))
