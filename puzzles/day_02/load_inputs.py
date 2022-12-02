from typing import List, Tuple

InputType = List[Tuple[str, str]]


def get_raw_input() -> str:
    with open("./input.txt") as file:
        return file.read()


def transform_input(raw_input: str) -> InputType:
    output_vals = []

    for line in raw_input.split("\n"):
        if not line:
            continue

        output_vals.append(line.split(" "))

    return output_vals


def get_input() -> InputType:
    return transform_input(get_raw_input())
