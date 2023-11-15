from typing import List, Tuple

from utils.input_deformatter import InputDeformatter

Position = Tuple[int, int]
InputType = List[Tuple[Position, Position]]


def parse_coordinates(desc: str) -> Tuple[Position, Position]:
    desc = desc.lstrip("Sensor at x=")
    sensor_x, desc = desc.split(", y=", maxsplit=1)
    sensor_y, desc = desc.split(": closest beacon is at x=")
    closest_x, closest_y = desc.split(", y=")

    return (int(sensor_x), int(sensor_y)), (int(closest_x), int(closest_y))


input_reader = InputDeformatter(
    cast_inner_type=parse_coordinates
)
