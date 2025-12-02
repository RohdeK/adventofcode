from puzzles.day_02.load_inputs import input_reader, InputType


def is_invalid(val: int, base: int) -> bool:
    valstr = str(val)

    if len(valstr) % base != 0:
        return False

    part_len = len(valstr) // base
    pattern = valstr[:part_len]

    for i in range(base):
        if valstr[i*part_len:(i+1)*part_len] != pattern:
            return False

    return True


def find_invalid_ids(rng: tuple[int, int]) -> list[int]:
    invalids = []

    for val in range(rng[0], rng[1] + 1):
        for base in range(2, len(str(val)) + 1):
            if is_invalid(val, base):
                invalids.append(val)
                break

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
