from typing import List

from utils.input_deformatter import InputDeformatter

InputType = List[List[int]]

input_reader = InputDeformatter[InputType](
    on_empty_primary_split="sub_split",
    cast_inner_type=int,
)
