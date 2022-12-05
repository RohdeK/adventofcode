from typing import List, Tuple

from puzzles.day_05.load_inputs import input_reader, InputType


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


def parse_slots(description: str) -> List[List[str]]:
    heights = description.split("\n")
    heights.reverse()

    slots_def = heights[0]
    slots_indices = [idx for idx, x in enumerate(slots_def) if x != " "]
    slots = [[] for _ in slots_indices]

    for height_row in heights[1:]:
        for slot_index, slot_desc_index in enumerate(slots_indices):
            try:
                slot_content = height_row[slot_desc_index]
            except IndexError:
                continue

            if slot_content != " ":
                slots[slot_index].append(slot_content)

    return slots


def parse_move(description: str) -> Tuple[int, int, int]:
    description, to_slot = description.split(" to ")
    description, from_slot = description.split(" from ")
    _, amount = description.split("move ")

    return int(from_slot), int(to_slot), int(amount)


def calculate_solution(input_values: InputType) -> int:
    stack_desc, move_descs = input_values
    stacking = Stackings(parse_slots(stack_desc))

    for move_desc in move_descs:
        from_slot, to_slot, amount = parse_move(move_desc)

        stacking.move_many(from_slot, to_slot, amount)

    return "".join(stacking.tops())


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
