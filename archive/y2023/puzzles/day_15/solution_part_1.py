from archive.y2023.puzzles.day_15.load_inputs import input_reader, InputType


def hash_string(value: str) -> int:
    curr_hash = 0

    for char in value:
        curr_hash += ord(char)
        curr_hash *= 17
        curr_hash %= 256

    return curr_hash


def calculate_solution(input_values: InputType) -> int:
    return sum(hash_string(v) for v in input_values)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
