from typing import Dict, List

from puzzles.day_05.load_inputs import Map, input_reader, InputType


def seed_to_location(seed_val: int, maps_by_from_type: Dict[str, Map]) -> int:
    current_type = "seed"
    current_value = seed_val

    while current_type != "location":
        m = maps_by_from_type[current_type]
        current_value = m.map_entry(current_value)
        current_type = m.to_type

    return current_value


def calculate_solution(input_values: InputType) -> int:
    source_seeds: List[int] = input_values[0]
    maps: List[Map] = input_values[1:]
    maps_by_from_type = {
        m.from_type: m for m in maps
    }

    location_nums = [seed_to_location(seed, maps_by_from_type) for seed in source_seeds]

    return min(location_nums)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
