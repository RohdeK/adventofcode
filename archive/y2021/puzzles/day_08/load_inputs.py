from typing import List

from utils.input_deformatter import InputDeformatter

InputType = List[str]


def get_raw_input() -> str:
    with open("./input.txt") as file:
        return file.read()


def transform_input(raw_input: str) -> InputType:
    return InputDeformatter[InputType]().load(raw_input)


def get_input() -> InputType:
    return transform_input(get_raw_input())
