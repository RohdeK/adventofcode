from typing import List, Tuple

from utils.input_deformatter import InputDeformatter

InputType = List[Tuple[str, str]]


def get_raw_input() -> str:
    with open("./input.txt") as file:
        return file.read()


def transform_input(raw_input: str) -> InputType:
    return InputDeformatter[InputType](
        inline_secondary_split=" ",
    ).load(raw_input)


def get_input() -> InputType:
    return transform_input(get_raw_input())