from dataclasses import dataclass
from typing import List

from utils.input_deformatter import InputDeformatter


@dataclass
class Valve:
    valve_name: str
    flow_rate: int
    connected_to: List[str]


def parse_valve(desc: str) -> Valve:
    _, desc = desc.split("Valve ")
    name, desc = desc.split(" has flow rate=")
    flow_rate, desc = desc.split(";")
    try:
        _, desc = desc.split("valves ")
    except ValueError:
        _, desc = desc.split("valve ")

    connected_to = desc.split(", ")

    return Valve(
        valve_name=name,
        flow_rate=int(flow_rate),
        connected_to=connected_to,
    )


InputType = List[Valve]

input_reader = InputDeformatter(
    cast_inner_type=parse_valve,
)
