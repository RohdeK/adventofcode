from dataclasses import dataclass
from typing import List, Optional, Union

from utils.input_deformatter import InputDeformatter


@dataclass
class MapRange:
    destination_start: int
    source_start: int
    range_length: int

    def map_entry(self, value: int) -> Optional[int]:
        if self.source_start <= value < self.source_start + self.range_length:
            return self.destination_start + value - self.source_start
        else:
            return None


@dataclass
class Map:
    from_type: str
    to_type: str
    ranges: List[MapRange]

    def map_entry(self, value: int) -> int:
        for r in self.ranges:
            target = r.map_entry(value)
            if target is not None:
                return target

        return value


InputType = List[Union[List[int], Map]]


def unpack_map(something: str) -> Union[List[int], Map]:
    lines = [v.strip() for v in something.split("\n")]
    descriptor = lines[0]
    content = lines[1:]

    if descriptor.startswith("seeds:"):
        return [int(c) for c in descriptor[7:].split()]

    descriptor, _ = descriptor.split(" ")
    from_type, to_type = descriptor.split("-to-")

    this_map = Map(from_type=from_type, to_type=to_type, ranges=[])

    for r in content:
        ds, ss, rl = map(int, r.split())
        this_map.ranges.append(MapRange(destination_start=ds, source_start=ss, range_length=rl))

    return this_map


input_reader = InputDeformatter[InputType](
    input_primary_split="\n\n",
    cast_inner_type=unpack_map,
)
