from dataclasses import dataclass
from typing import List, Tuple

from utils.input_deformatter import InputDeformatter


@dataclass
class Locator:
    from_: str
    left_: str
    right_: str


InputType = Tuple[List[str], List[Locator]]


def parse_locators(raw_locators: str) -> Locator:
    from_, rest = raw_locators.strip().split(" = ")
    left_, right_ = rest.strip("()").split(", ")
    return Locator(from_=from_, left_=left_, right_=right_)


input_reader = InputDeformatter[InputType](
    input_primary_split="\n\n",
    inline_secondary_split="\n",
    cast_inner_type=[str, parse_locators]
)
