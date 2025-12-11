from utils.input_deformatter import InputDeformatter

InputType = list[tuple[str, list[str]]]

input_reader = InputDeformatter[InputType](
    inline_secondary_split=": ",
    cast_inner_type=lambda x: x.split(" ")
)
