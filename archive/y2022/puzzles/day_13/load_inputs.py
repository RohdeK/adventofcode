import ast
from typing import List, Tuple, Union

from utils.input_deformatter import InputDeformatter

NestedList = List[Union[int, "NestedList"]]

InputType = List[Tuple[NestedList, NestedList]]

input_reader = InputDeformatter(
    input_primary_split="\n\n",
    inline_secondary_split="\n",
    cast_inner_type=ast.literal_eval,
)
