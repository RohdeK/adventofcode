from typing import List, Tuple

from utils.input_deformatter import InputDeformatter

InputType = List[Tuple[Tuple[int, int], Tuple[int, int]]]


def from_to_cast(val: str) -> Tuple[int, int]:
    from_val, to_val = val.split("-")
    return int(from_val), int(to_val)


input_reader = InputDeformatter[InputType](
    inline_secondary_split=",",
    cast_inner_type=from_to_cast,
)
