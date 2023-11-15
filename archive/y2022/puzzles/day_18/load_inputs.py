from typing import List, Tuple

from utils.input_deformatter import InputDeformatter

Cubelet = Tuple[int, int, int]
InputType = List[Cubelet]

input_reader = InputDeformatter(
    inline_secondary_split=",",
    cast_inner_type=int,
)
