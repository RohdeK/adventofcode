from puzzles.day_13.load_inputs import input_reader, InputType
from puzzles.day_13.solution_part_1 import fastest_route_cost


def calculate_solution(input_values: InputType) -> int:
    checksum = 0

    for setup in input_values:
        upped_prize = (setup[2][0] + 10000000000000, setup[2][1] + 10000000000000)
        checksum += fastest_route_cost(setup[0], setup[1], upped_prize)

    return checksum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
