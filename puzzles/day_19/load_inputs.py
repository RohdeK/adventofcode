from utils.input_deformatter import InputDeformatter

InputType = tuple[list[str], list[str]]

input_reader = InputDeformatter[InputType](
    input_primary_split="\n\n",
    cast_inner_type=[lambda x: x.split(", "), lambda x: x.split("\n")],
)
