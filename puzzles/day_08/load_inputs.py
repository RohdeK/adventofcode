from typing import List

from utils.input_deformatter import InputDeformatter

InputType = List[List[int]]

input_reader = InputDeformatter(
    inline_secondary_split="",
    cast_inner_type=int,
)
