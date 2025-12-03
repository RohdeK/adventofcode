from puzzles.day_03.load_inputs import input_reader, InputType


def find_max_joltage(bank: list[int]) -> int:
    tenner = max(bank[:-1])
    tenner_idx = bank.index(tenner)
    onner = max(bank[(tenner_idx+1):])

    return int(f"{tenner}{onner}")


def calculate_solution(input_values: InputType) -> int:
    total_joltage = 0

    for bank in input_values:
        total_joltage += find_max_joltage(bank)

    return total_joltage


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
