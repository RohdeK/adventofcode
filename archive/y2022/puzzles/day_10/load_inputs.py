from typing import List

from utils.input_deformatter import InputDeformatter


class Operation:
    def __init__(self, cycle_length: int):
        self.cycle_length = cycle_length


class Noop(Operation):
    def __init__(self):
        super().__init__(1)

    def __repr__(self):
        return "noop"


class Addx(Operation):
    def __init__(self, value: int):
        super().__init__(2)
        self.value = value

    def __repr__(self):
        return f"addx {self.value}"


def parse_operation(opdesc: str) -> Operation:
    if opdesc == "noop":
        return Noop()
    else:
        _, val = opdesc.split(" ")
        return Addx(int(val))


InputType = List[Operation]

input_reader = InputDeformatter(
    cast_inner_type=parse_operation
)

