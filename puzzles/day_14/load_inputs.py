from utils.common_structures.planar_map import Position
from utils.input_deformatter import InputDeformatter

InputType = list[tuple[Position, Position]]


def unpack_two_dim(p_or_v: str) -> Position:
    v1, v2 = p_or_v.strip("pv=").split(",")
    return int(v1), int(v2)


input_reader = InputDeformatter[InputType](
    inline_secondary_split=" ",
    cast_inner_type=unpack_two_dim,
)
