from typing import List

from utils.common_structures.planar_map import Location, parse_map_lines
from utils.input_deformatter import InputDeformatter


InputType = List[List[Location]]

input_reader = InputDeformatter(
    input_primary_split=None,
    cast_inner_type=parse_map_lines,
)
