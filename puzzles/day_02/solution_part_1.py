from puzzles.day_02.load_inputs import input_reader, InputType


def is_invalid(val: int) -> bool:
    valstr = str(val)
    half_len = len(valstr) // 2

    if len(valstr) % 2 == 1:
        return False

    return valstr[:half_len] == valstr[half_len:]


def find_invalid_ids(rng: tuple[int, int]) -> list[int]:
    invalids = []

    for val in range(rng[0], rng[1] + 1):
        if is_invalid(val):
            invalids.append(val)

    return invalids


def calculate_solution(input_values: InputType) -> int:
    total_invalids = []

    for rng in input_values:
        invalids = find_invalid_ids(rng)
        print(rng, invalids)
        total_invalids.extend(invalids)

    return sum(total_invalids)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
