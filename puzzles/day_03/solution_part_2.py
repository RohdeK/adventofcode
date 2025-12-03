from puzzles.day_03.load_inputs import input_reader, InputType


def find_max_joltage(bank: list[int], size: int) -> int:
    final_num = ""

    idx = 0

    for isize in range(size, 0, -1):
        locked = isize - 1
        if locked > 0:
            moveable_slice = bank[idx:-locked]
        else:
            moveable_slice = bank[idx:]

        next_num = max(moveable_slice)
        next_idx = bank[idx:].index(next_num)

        final_num += str(next_num)
        idx += next_idx + 1

    return int(final_num)


def calculate_solution(input_values: InputType) -> int:
    total_joltage = 0

    for bank in input_values:
        total_joltage += find_max_joltage(bank, 12)

    return total_joltage


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
