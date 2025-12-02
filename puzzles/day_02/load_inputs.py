from utils.input_deformatter import InputDeformatter

InputType = list[tuple[int, int]]

input_reader = InputDeformatter[InputType](
    input_primary_split=",",
    inline_secondary_split="-",
    cast_inner_type=int,
)
