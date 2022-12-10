from typing import Callable

from puzzles.day_10.load_inputs import Addx, Noop, Operation, input_reader, InputType


class Device:
    def __init__(self):
        self.cycle = 0
        self.x = 1
        self.on_after_cycle_callback: Callable[[int, int], None] = None
        self.on_during_cycle_callback: Callable[[int, int], None] = None

    def on_after_cycle(self) -> None:
        self.on_after_cycle_callback and self.on_after_cycle_callback(self.cycle, self.x)

    def on_during_cycle(self) -> None:
        self.on_during_cycle_callback and self.on_during_cycle_callback(self.cycle + 1, self.x)

    def run_op(self, op: Operation) -> None:
        if isinstance(op, Noop):
            self.on_during_cycle()
            self.cycle += 1
            self.on_after_cycle()

        elif isinstance(op, Addx):
            self.on_during_cycle()
            self.cycle += 1
            self.on_after_cycle()

            self.on_during_cycle()
            self.cycle += 1
            self.x += op.value
            self.on_after_cycle()


def calculate_solution(input_values: InputType) -> int:
    start = Device()

    score = 0

    def add_score(cycle: int, x: int) -> None:
        nonlocal score
        if cycle % 40 == 20:
            score += cycle * x

    start.on_during_cycle_callback = add_score

    for op in input_values:
        start.run_op(op)

    return score


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
