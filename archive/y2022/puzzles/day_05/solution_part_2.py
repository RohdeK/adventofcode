from archive.y2022.puzzles.day_05.load_inputs import InputType, input_reader
from archive.y2022.puzzles.day_05.solution_part_1 import Stackings


class Stackings2(Stackings):
    def move_many(self, from_slot: int, to_slot: int, amount: int) -> None:
        move_stack = [self.slots[from_slot - 1].pop() for _ in range(amount)]
        move_stack.reverse()
        self.slots[to_slot - 1].extend(move_stack)


def calculate_solution(input_values: InputType) -> int:
    stacks, moves = input_values
    stacking = Stackings2(stacks)

    for from_slot, to_slot, amount in moves:
        stacking.move_many(from_slot, to_slot, amount)

    return "".join(stacking.tops())


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
