from typing import List

from puzzles.day_22.load_inputs import Location, parse_map_lines
from utils.input_deformatter import InputDeformatter


InputType = List[List[Location]]

input_reader = InputDeformatter(
    input_primary_split=None,
    cast_inner_type=parse_map_lines,
)
