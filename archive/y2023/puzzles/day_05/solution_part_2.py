from typing import Dict, List, Optional, Tuple

from archive.y2023.puzzles.day_05.load_inputs import Map, MapRange, input_reader, InputType
from utils.common_structures.num_range import NumRange


class CoolerMapRange:
    def __init__(self, regular_range: MapRange):
        self.source_range = NumRange(
            from_=regular_range.source_start,
            range_=regular_range.range_length,
        )
        self.dest_range = NumRange(
            from_=regular_range.destination_start,
            range_=regular_range.range_length,
        )

    def map_range(self, rng: NumRange) -> Tuple[Optional[NumRange], List[NumRange]]:
        mappable_range = rng.intersect(self.source_range)
        if mappable_range:
            mappable_range = NumRange(
                from_=mappable_range.from_ + self.dest_range.from_ - self.source_range.from_,
                range_=mappable_range.range_,
            )

        unmappable_ranges = rng.minus(self.source_range)

        return mappable_range, unmappable_ranges


class CoolerMap:
    def __init__(self, regular_map: Map):
        self.from_type = regular_map.from_type
        self.to_type = regular_map.to_type
        self.ranges = [CoolerMapRange(r) for r in regular_map.ranges]

    def map_range(self, rng: NumRange) -> List[NumRange]:
        ranges_solved = []
        ranges_to_solve = [rng]

        for r in self.ranges:
            remaining_to_solve = []
            for rng in ranges_to_solve:
                solved, unsolved = r.map_range(rng)
                if solved:
                    ranges_solved.append(solved)
                remaining_to_solve.extend(unsolved)
            ranges_to_solve = remaining_to_solve

        return [*ranges_to_solve, *ranges_solved]


def seed_to_location(seed_val: NumRange, maps_by_from_type: Dict[str, CoolerMap]) -> List[NumRange]:
    current_type = "seed"
    current_values = [seed_val]

    while current_type != "location":
        iter_values = []
        m = maps_by_from_type[current_type]
        for v in current_values:
            mapped = m.map_range(v)
            iter_values.extend(mapped)
        current_type = m.to_type
        current_values = iter_values

    return current_values


def calculate_solution(input_values: InputType) -> int:
    source_seed_ranges: List[int] = input_values[0]
    maps: List[Map] = input_values[1:]
    maps_by_from_type = {
        m.from_type: CoolerMap(m) for m in maps
    }

    min_locations = []

    for seed_start, seed_range in zip(source_seed_ranges[::2], source_seed_ranges[1::2]):
        rng = NumRange(from_=seed_start, range_=seed_range)
        locs = seed_to_location(rng, maps_by_from_type)

        min_locations.extend([lo.from_ for lo in locs])

    return min(min_locations)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
