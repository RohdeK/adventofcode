from utils.input_deformatter import InputDeformatter

InputType = list[int]

input_reader = InputDeformatter[InputType](
    input_primary_split=" ",
    cast_inner_type=int,
)
