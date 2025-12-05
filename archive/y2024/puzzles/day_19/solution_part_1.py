from archive.y2024.puzzles.day_19.load_inputs import input_reader, InputType


def can_weave(pattern: str, building_blocks: list[str]) -> int:
    for b in building_blocks:
        if b == pattern:
            return True

        if pattern.startswith(b):
            if can_weave(pattern[len(b):], building_blocks):
                return True

    return False


def calculate_solution(input_values: InputType) -> int:
    bblocks = input_values[0]

    solveable_patterns = 0

    for pattern in input_values[1]:
        if can_weave(pattern, bblocks):
            solveable_patterns += 1

    return solveable_patterns


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
