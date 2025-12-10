from dataclasses import dataclass

from utils.input_deformatter import InputDeformatter


@dataclass
class Machine:
    target_state: list[bool]
    buttons: list[list[int]]
    joltages: list[int]


def to_machine(input_line: str) -> Machine:
    target_state = None
    buttons = []
    joltages = None

    for x in input_line.split(" "):
        if x.startswith("[") and x.endswith("]"):
            target_state = [y == "#" for y in x.strip("[]")]

        elif x.startswith("(") and x.endswith(")"):
            buttons.append(list(map(int, x.strip("()").split(","))))

        elif x.startswith("{") and x.endswith("}"):
            joltages = list(map(int, x.strip("{}").split(",")))

        else:
            raise ValueError(x)

    return Machine(
        target_state=target_state,
        joltages=joltages,
        buttons=buttons,
    )


InputType = list[Machine]

input_reader = InputDeformatter[InputType](
    cast_inner_type=to_machine
)
