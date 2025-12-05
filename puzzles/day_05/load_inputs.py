from utils.input_deformatter import InputDeformatter

InputType = tuple[list[range], list[int]]


def to_range(rng: str) -> range:
    r_from, r_to = map(int, rng.split("-"))

    return range(r_from, r_to + 1)


input_reader = InputDeformatter[InputType](
    input_primary_split="\n\n",
    inline_secondary_split="\n",
    cast_inner_type=[to_range, int]
)
