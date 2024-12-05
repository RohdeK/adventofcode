from utils.input_deformatter import InputDeformatter

InputType = tuple[list[tuple[int, int]], list[list[int]]]


def parse_rule(order_rule: str) -> tuple[int, int]:
    bef, aft = order_rule.split("|")
    return int(bef), int(aft)


def parse_sequence(sequence: str) -> list[int]:
    return [int(val) for val in sequence.split(",")]


input_reader = InputDeformatter[InputType](
    input_primary_split="\n\n",
    inline_secondary_split="\n",
    cast_inner_type=[parse_rule, parse_sequence]
)
