
from archive.y2022.puzzles.day_10.load_inputs import input_reader, InputType
from archive.y2022.puzzles.day_10.solution_part_1 import Device


def calculate_solution(input_values: InputType) -> int:
    start = Device()

    linearized_screen = ""

    def light_pixel(cycle: int, x: int) -> None:
        nonlocal linearized_screen

        pixel_line_pos = (cycle - 1) % 40

        if pixel_line_pos in (x - 1, x, x + 1):
            linearized_screen += "#"
        else:
            linearized_screen += "."

    start.on_during_cycle_callback = light_pixel

    for op in input_values:
        start.run_op(op)

    wrapped_screen = ""
    rows = 0

    while len(linearized_screen) > 40:
        rows += 1
        wrapped_screen += linearized_screen[:40] + "\n"
        linearized_screen = linearized_screen[40:]

    wrapped_screen += linearized_screen

    return wrapped_screen


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
