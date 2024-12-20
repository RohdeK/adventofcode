from typing import Callable

from puzzles.day_17.load_inputs import input_reader, InputType


class Computer:
    def __init__(self, reg_a: int, reg_b: int, reg_c: int):
        self.A = reg_a
        self.B = reg_b
        self.C = reg_c
        self.output = []
        self.program = []
        self.pointer = 0

    def run(self, program: list[int]) -> str:
        self.program = program
        self.output = []
        self.pointer = 0

        while self.pointer < len(self.program):
            opcode, operand = self.program[self.pointer], self.program[self.pointer + 1]
            self.operation(opcode)(operand)
            self.pointer += 2

        return ",".join(map(str, self.output))

    def operation(self, opcode: int) -> Callable[[int], None]:
        return {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }[opcode]

    def combo(self, operand: int) -> int:
        return {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: self.A,
            5: self.B,
            6: self.C,
        }[operand]

    def adv(self, combo: int) -> None:
        self.A = int(self.A / (2 ** self.combo(combo)))

    def bxl(self, literal: int) -> None:
        self.B = self.B ^ literal

    def bst(self, combo: int) -> None:
        self.B = self.combo(combo) % 8

    def jnz(self, literal: int) -> None:
        if self.A == 0:
            return

        self.pointer = literal - 2

    def bxc(self, _combo: int) -> None:
        self.B = self.B ^ self.C

    def out(self, combo: int) -> None:
        self.output.append(self.combo(combo) % 8)

    def bdv(self, combo: int) -> None:
        self.B = int(self.A / (2 ** self.combo(combo)))

    def cdv(self, combo: int) -> None:
        self.C = int(self.A / (2 ** self.combo(combo)))


def calculate_solution(input_values: InputType) -> str:
    computer = Computer(*input_values[0])
    return computer.run(input_values[1])


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
