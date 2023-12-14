from puzzles.day_14.load_inputs import input_reader, InputType
from puzzles.day_14.solution_part_1 import BoulderMap


def calculate_solution(input_values: InputType) -> int:
    print("\n")
    bmap = BoulderMap(input_values[0])

    roll_order = ["north", "west", "south", "east"]

    for i in range(3):
        for r in roll_order:
            bmap.roll(r)

        print(bmap)

    return bmap.sum_weights()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
