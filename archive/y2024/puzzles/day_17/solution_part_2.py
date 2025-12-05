from archive.y2024.puzzles.day_17.load_inputs import input_reader, InputType
from archive.y2024.puzzles.day_17.solution_part_1 import Computer


class Inconsistent(Exception):
    pass


class SelfOptimizingComputer(Computer):
    def __init__(self):
        super().__init__(0, 0, 0)

    def reset(self, a: int) -> None:
        self.A = a
        self.B = 0
        self.C = 0

    def out(self, combo: int) -> None:
        super().out(combo)

        if self.output != self.program[:len(self.output)]:
            raise Inconsistent()

    def optimize_for(self, program: list[int]) -> int:
        a_value = -1
        while True:
            a_value += 1
            self.reset(a_value)

            try:
                self.run(program)
            except Inconsistent:
                continue

            if self.output != program:
                continue

            return a_value


def calculate_solution(input_values: InputType) -> int:
    order = [4, 4, 6, 7, 0, 1, 2, 3]

    for i in range(8):
        j = (
                i * 2**47 +
                i * 2 ** 44 // 8 +
                i * 2 ** 41 // 8 +
                i * 2 ** 38 // 8 +
                i * 2 ** 35 // 8 +
                i * 2 ** 32 // 8 +
                i * 2 ** 29 // 8 +
                i * 2 ** 26 // 8 +
                i * 2 ** 23 // 8 +
                i * 2 ** 20 // 8 +
                i * 2 ** 18 // 8 +
                i * 2 ** 15 // 8 +
                i * 2 ** 12 // 8 +
                i * 2 ** 9 // 8 +
                i * 2 ** 6 // 8 +
                i * 2 ** 3 // 8 +
                i * 2 ** 0 // 8
        )
        computer = Computer(j, 0, 0)
        print(i, computer.run(input_values[1]))

    # return computer.optimize_for(input_values[1])

if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))


    """
Register A: 64854237
Register B: 0
Register C: 0

Program: 2,4,1,1,7,5,1,5,4,0,5,5,0,3,3,0

101010101100
101
bst(A)
    B = A % 8
bxl(1)
    B = B xor 1
cdv(B)
    C = A // B
bxl(5)
    B = B xor 5
bxc
    B = B xor C
out(B)
    B % 8
adv(3)
    A = A // 8
jump(0)
"""
"""
last B = 0
B == C



"""
