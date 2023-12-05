from typing import Dict, List, Optional, Tuple

from puzzles.day_05.load_inputs import Map, MapRange, input_reader, InputType


class Range:
    def __init__(self, from_value: int, range_value: int):
        self.from_value = from_value
        self.range_value = range_value

    def __repr__(self):
        return f"[{self.from_value}:{self.to_value}]"

    @property
    def to_value(self) -> int:
        return self.from_value + self.range_value - 1

    def overlap(self, other: "Range") -> Optional["Range"]:
        if other.from_value < self.from_value:
            if other.to_value < self.from_value:
                return None
            elif other.to_value <= self.to_value:
                return Range(self.from_value, other.to_value - self.from_value + 1)
            else:
                return self
        elif other.from_value <= self.to_value:
            if other.to_value <= self.to_value:
                return other
            else:
                return Range(other.from_value, self.to_value - other.from_value + 1)
        else:
            return None

    def underlap(self, other: "Range") -> List["Range"]:
        underlaps = []

        if self.from_value < other.from_value:
            range_val = min(
                other.from_value - self.from_value,
                self.range_value,
            )
            underlaps.append(Range(self.from_value, range_val))
        if self.to_value > other.to_value:
            max_start = max(
                other.to_value + 1,
                self.from_value,
            )
            underlaps.append(Range(max_start, self.to_value - max_start + 1))
        return underlaps


class CoolerMapRange:
    def __init__(self, regular_range: MapRange):
        self.source_range = Range(regular_range.source_start, regular_range.range_length)
        self.dest_range = Range(regular_range.destination_start, regular_range.range_length)

    def map_range(self, rng: Range) -> Tuple[Optional[Range], List[Range]]:
        mappable_range = rng.overlap(self.source_range)
        if mappable_range:
            mappable_range = Range(
                mappable_range.from_value + self.dest_range.from_value - self.source_range.from_value,
                mappable_range.range_value,
            )

        unmappable_ranges = rng.underlap(self.source_range)

        return mappable_range, unmappable_ranges


class CoolerMap:
    def __init__(self, regular_map: Map):
        self.from_type = regular_map.from_type
        self.to_type = regular_map.to_type
        self.ranges = [CoolerMapRange(r) for r in regular_map.ranges]

    def map_range(self, rng: Range) -> List[Range]:
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


def seed_to_location(seed_val: Range, maps_by_from_type: Dict[str, CoolerMap]) -> List[Range]:
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
        rng = Range(seed_start, seed_range)
        locs = seed_to_location(rng, maps_by_from_type)

        min_locations.extend([l.from_value for l in locs])

    return min(min_locations)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
