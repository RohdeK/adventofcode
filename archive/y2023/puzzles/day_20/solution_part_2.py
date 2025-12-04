from functools import reduce

from archive.y2023.puzzles.day_08.solution_part_2 import lcm
from archive.y2023.puzzles.day_20.load_inputs import input_reader, InputType
from archive.y2023.puzzles.day_20.solution_part_1 import Module, Orchestrator, Signal


class Finished(Exception):
    pass


class BreakerModule(Module):
    def __init__(self, name: str):
        super().__init__(name, [])

    def handle(self, signal: Signal, _source: Signal) -> None:
        if signal == Signal.LOW:
            raise Finished()


def calculate_solution(input_values: InputType) -> int:
    orch = Orchestrator()
    orch.add_modules(input_values)

    orch.modules["rx"] = BreakerModule("rx")

    backoff_print = 1
    button_presses = 0
    while True:
        try:
            button_presses += 1
            orch.press_button()

            if button_presses == backoff_print:
                print(button_presses)
                backoff_print *= 2
        except Finished:
            return button_presses


if __name__ == "__main__":
    print(reduce(lcm, [3739, 4027, 3793, 3923]))
    exit(0)

    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
