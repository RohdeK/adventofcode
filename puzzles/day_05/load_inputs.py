import re
from typing import List, Tuple

from utils.input_deformatter import InputDeformatter

InputType = Tuple[str, List[str]]

input_reader = InputDeformatter(
    input_primary_split=re.compile(r"\n\s*\n"),
    inline_secondary_split=[None, "\n"],
    strip_primary_split=False,
    strip_secondary_split=True,
    empty_secondary_boundary_strategy="strip",
)
