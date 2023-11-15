from typing import List

from utils.input_deformatter import InputDeformatter

InputType = List[List[str]]

input_reader = InputDeformatter(
    inline_secondary_split="",
)
