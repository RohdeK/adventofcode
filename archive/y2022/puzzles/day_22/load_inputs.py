from dataclasses import dataclass
from typing import List, Tuple

from utils.common_structures.planar_map import Location, parse_map_lines
from utils.input_deformatter import InputDeformatter


class Movement:
    pass


@dataclass
class Turn(Movement):
    direction: str


@dataclass
class Walk(Movement):
    distance: int


def parse_directions(input_desc: str) -> List[Movement]:
    movement_list = []

    split_by_right = input_desc.split("R")

    for sub_input in split_by_right:
        split_by_left = sub_input.split("L")
        sublist = [None] * (len(split_by_left) * 2 - 1)
        sublist[::2] = [Walk(distance=int(d)) for d in split_by_left]
        sublist[1::2] = [Turn(direction="L") for _ in range(len(split_by_left) - 1)]

        movement_list.extend(sublist)
        movement_list.append(Turn(direction="R"))

    movement_list.pop()

    return movement_list


InputType = Tuple[List[Location], List[Movement]]

input_reader = InputDeformatter(
    input_primary_split="\n\n",
    strip_primary_split=False,
    cast_inner_type=[parse_map_lines, parse_directions],
)
