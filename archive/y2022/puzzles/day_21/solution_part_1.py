from collections import deque

from archive.y2022.puzzles.day_21.load_inputs import input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    input_values = [line.replace(": ", " = ") for line in input_values]
    non_evalled = deque(input_values)
    local_dict = {}

    while len(non_evalled):
        next_command = non_evalled.popleft()
        try:
            exec(next_command, globals(), local_dict)
        except NameError:
            non_evalled.append(next_command)

    return local_dict["root"]


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
