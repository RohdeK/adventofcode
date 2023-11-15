from typing import List, Tuple

from archive.y2022.puzzles.day_05.load_inputs import input_reader, InputType


class Stackings:
    def __init__(self, slots: List[List[str]]):
        self.slots = slots

    def move_many(self, from_slot: int, to_slot: int, amount: int) -> None:
        for _ in range(amount):
            self.move_one(from_slot, to_slot)

    def move_one(self, from_slot: int, to_slot: int) -> None:
        self.slots[to_slot - 1].append(self.slots[from_slot - 1].pop())

    def tops(self) -> List[str]:
        tops_list = []

        for slot in self.slots:
            if not slot:
                continue

            tops_list.append(slot[-1])

        return tops_list


def calculate_solution(input_values: InputType) -> int:
    stacks, moves = input_values
    stacking = Stackings(stacks)

    for from_slot, to_slot, amount in moves:
        stacking.move_many(from_slot, to_slot, amount)

    return "".join(stacking.tops())


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
