from utils.input_deformatter import InputDeformatter

InputType = list[tuple[int, list[int]]]


def parse_inner(line: str) -> tuple[int, list[int]]:
    calc, comp = line.split(": ")
    comps = [int(c) for c in comp.split(" ")]
    return int(calc), comps


input_reader = InputDeformatter[InputType](
    cast_inner_type=parse_inner,
)
