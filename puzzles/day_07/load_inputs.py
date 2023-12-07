from typing import List, Tuple

from utils.input_deformatter import InputDeformatter

InputType = List[Tuple[str, int]]

input_reader = InputDeformatter[InputType](
    inline_secondary_split=" ",
)
