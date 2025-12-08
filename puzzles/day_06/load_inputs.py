from utils.input_deformatter import InputDeformatter

InputType = str


input_reader = InputDeformatter[InputType](
    input_primary_split=None,
)
