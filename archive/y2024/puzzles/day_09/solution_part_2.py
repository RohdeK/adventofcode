from typing import Optional, Union

from archive.y2024.puzzles.day_09.load_inputs import input_reader, InputType


class Slot:
    def __init__(self, size: int, empty: bool, iden: int):
        self.size = size
        self.empty = empty
        self.id = iden


class FileSlot(Slot):
    next_id = -1

    def __init__(self, size: int):
        super().__init__(size, False, self.new_id())

    def __repr__(self) -> str:
        return f"[{str(self.id) * self.size}]"

    @classmethod
    def new_id(cls) -> int:
        cls.next_id += 1
        return cls.next_id


class EmptySlot(Slot):
    def __init__(self, size: int):
        super().__init__(size, True, 0)

    def __repr__(self) -> str:
        return "." * self.size


class FileRegister:
    def __init__(self, rep: str):
        self.slots: list[Slot] = []
        self.parse_rep(rep)

    def __repr__(self) -> str:
        string = ""
        for slot in self.slots:
            string += str(slot)
        return string

    def parse_rep(self, rep: str) -> None:
        is_file = True

        for char in rep:
            size = int(char)

            if is_file:
                self.slots.append(FileSlot(size))
            else:
                self.slots.append(EmptySlot(size))

            is_file = not is_file

    def defragment(self) -> None:
        iter_position = len(self.slots)
        max_considered_index = None

        while iter_position >= 0:
            iter_position -= 1

            current_slot = self.slots[iter_position]

            if current_slot.empty:
                continue

            if max_considered_index is not None and current_slot.id > max_considered_index:
                continue

            max_considered_index = current_slot.id

            empty_index , empty_fit = next(
                ((i, s) for i, s in enumerate(self.slots) if s.empty and s.size >= current_slot.size), (None, None)
            )

            if empty_fit is None:
                continue

            if iter_position < empty_index:
                continue

            replaced = self.slots.pop(iter_position)

            self.slots.insert(iter_position, EmptySlot(current_slot.size))

            if empty_fit.size == current_slot.size:
                self.slots[empty_index] = replaced
            else:
                empty_fit.size -= current_slot.size
                self.slots.insert(empty_index, replaced)

    def calculate_checksum(self) -> int:
        iter_index = 0
        checksum = 0

        for slot in self.slots:
            for _ in range(slot.size):
                checksum += slot.id * iter_index
                iter_index += 1

        return checksum


def calculate_solution(input_values: InputType) -> int:
    register = FileRegister(input_values)
    register.defragment()
    return register.calculate_checksum()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
