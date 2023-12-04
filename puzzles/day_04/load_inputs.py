from typing import List, Tuple

from utils.input_deformatter import InputDeformatter

InputType = List[Tuple[List[int], List[int]]]


def extract_number_list(line_segment: str) -> List[int]:
    if line_segment.startswith("Card"):
        _, line_segment = line_segment.split(": ")

    return [int(v) for v in line_segment.split()]


input_reader = InputDeformatter[InputType](
    inline_secondary_split="|",
    strip_secondary_split=True,
    cast_inner_type=extract_number_list
)
