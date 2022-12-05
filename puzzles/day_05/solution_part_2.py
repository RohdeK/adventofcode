from puzzles.day_05.load_inputs import InputType, input_reader
from puzzles.day_05.solution_part_1 import Stackings, parse_move, parse_slots


class Stackings2(Stackings):
    def move_many(self, from_slot: int, to_slot: int, amount: int) -> None:
        move_stack = [self.slots[from_slot - 1].pop() for _ in range(amount)]
        move_stack.reverse()
        self.slots[to_slot - 1].extend(move_stack)


def calculate_solution(input_values: InputType) -> int:
    stack_desc, move_descs = input_values
    stacking = Stackings2(parse_slots(stack_desc))

    for move_desc in move_descs:
        from_slot, to_slot, amount = parse_move(move_desc)

        stacking.move_many(from_slot, to_slot, amount)

    return "".join(stacking.tops())


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
