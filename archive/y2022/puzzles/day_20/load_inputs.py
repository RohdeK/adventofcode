from typing import List

from utils.input_deformatter import InputDeformatter

InputType = List[int]

input_reader = InputDeformatter(
    cast_inner_type=int,
)
