from utils.common_structures.planar_map import Direction, Location, parse_map_lines
from utils.input_deformatter import InputDeformatter

InputType = tuple[list[Location], list[Direction]]


def parse_direction_list(directions: str) -> list[Direction]:
    return [Direction.from_tile_rep(d) for d in directions.replace("\n", "")]


input_reader = InputDeformatter[InputType](
    input_primary_split="\n\n",
    cast_inner_type=[parse_map_lines, parse_direction_list],
)
