
from puzzles.day_12.load_inputs import input_reader, InputType
from puzzles.day_12.solution_part_1 import HeightGrid


class ModifiedHeightGrid(HeightGrid):
    @staticmethod
    def is_starting_point(height: str) -> bool:
        return height in ("a", "S")


def calculate_solution(input_values: InputType) -> int:
    return ModifiedHeightGrid(input_values).get_end_distance()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
