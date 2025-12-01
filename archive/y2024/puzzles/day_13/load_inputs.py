from utils.common_structures.planar_map import Position
from utils.input_deformatter import InputDeformatter

InputType = list[tuple[Position, Position, Position]]


def parse_button_setup(button_setup: str) -> tuple[Position, Position, Position]:
    button_a, button_b, prize = button_setup.split("\n")

    button_a_x, button_a_y = button_a.replace("Button A: ", "").split(", ")
    button_a_values = int(button_a_x.strip("X")), int(button_a_y.strip("Y"))

    button_b_x, button_b_y = button_b.replace("Button B: ", "").split(", ")
    button_b_values = int(button_b_x.strip("X")), int(button_b_y.strip("Y"))

    prize_x, prize_y = prize.replace("Prize: ", "").split(", ")
    prize_values = int(prize_x.strip("X=")), int(prize_y.strip("Y="))

    return button_a_values, button_b_values, prize_values


input_reader = InputDeformatter[InputType](
    input_primary_split="\n\n",
    cast_inner_type=parse_button_setup,
)
