from puzzles.day_24.load_inputs import input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    raise NotImplemented


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
