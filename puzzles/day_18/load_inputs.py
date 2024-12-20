from utils.common_structures.planar_map import Position
from utils.input_deformatter import InputDeformatter

InputType = list[Position]

input_reader = InputDeformatter[InputType](
    inline_secondary_split=",",
    cast_inner_type=int,
)
