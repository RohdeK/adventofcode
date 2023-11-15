from typing import List

from utils.input_deformatter import InputDeformatter

InputType = List[List[str]]

input_reader = InputDeformatter(
    input_primary_split="\n\n",
    inline_secondary_split="\n",
)
