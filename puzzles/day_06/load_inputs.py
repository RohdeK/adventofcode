from typing import List, Tuple

from utils.input_deformatter import InputDeformatter

InputType = Tuple[List[int], List[int]]


def extract_numbers(raw: str) -> List[int]:
    return [int(v) for v in raw[raw.index(":") + 1:].strip().split()]


input_reader = InputDeformatter[InputType](
    cast_inner_type=extract_numbers,
)
