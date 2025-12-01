from puzzles.day_19.load_inputs import input_reader, InputType


NUMCACHE = {}


def can_weave(pattern: str, building_blocks: list[str]) -> int:
    global NUMCACHE

    print(f"Checking {pattern}")

    if pattern in NUMCACHE:
        print("Retrieved from cache")
        return NUMCACHE[pattern]

    numfits = 0
    for b in building_blocks:
        if b == pattern:
            print(f"Found {pattern} directly")
            numfits += 1

        elif pattern.startswith(b):
            print(f"Deepening {pattern} with {b}")
            subfits = can_weave(pattern[len(b):], building_blocks)
            print(f"Found {subfits} for {pattern}: {b}")
            numfits += subfits

    print(f"Done with {pattern}, found {numfits} total.")
    NUMCACHE[pattern] = numfits

    return numfits


def calculate_solution(input_values: InputType) -> int:
    bblocks = input_values[0]

    solveable_patterns = 0

    for idx, pattern in enumerate(input_values[1]):
        numfits = can_weave(pattern, bblocks)
        print(f"{idx} solveable in {numfits} ways.")
        solveable_patterns += numfits

    return solveable_patterns


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
