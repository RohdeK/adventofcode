from typing import List, Tuple

from utils.input_deformatter import InputDeformatter

InputType = List[Tuple[str, int]]

input_reader = InputDeformatter(
    inline_secondary_split=" ",
    cast_inner_type=lambda x: int(x) if x.isnumeric() else x,
)
