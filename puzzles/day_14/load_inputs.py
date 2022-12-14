from typing import Tuple, List

from utils.input_deformatter import InputDeformatter

Position = Tuple[int, int]
InputType = List[List[Position]]


def split_tertiary(pair_desc: str) -> Tuple[int, int]:
    x, y = pair_desc.split(",")
    return int(x), int(y)


input_reader = InputDeformatter(
    inline_secondary_split=" -> ",
    cast_inner_type=split_tertiary,
)
