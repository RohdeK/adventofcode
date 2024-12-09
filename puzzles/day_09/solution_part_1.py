from typing import Optional

from puzzles.day_09.load_inputs import input_reader, InputType


class FileSlot:
    next_id = -1

    def __init__(self, id_val: int):
        self.id = id_val

    def __repr__(self) -> str:
        return f"[{self.id}]"

    @classmethod
    def new_id(cls) -> int:
        cls.next_id += 1
        return cls.next_id


class FileRegister:
    def __init__(self, rep: str):
        self.slots: list[Optional[FileSlot]] = []

        self.parse_rep(rep)

    def __repr__(self) -> str:
        string = ""
        for slot in self.slots:
            if slot is None:
                string += "."
            else:
                string += str(slot)
        return string

    def parse_rep(self, rep: str) -> None:
        is_file = True

        for char in rep:
            size = int(char)

            if is_file:
                file_id = FileSlot.new_id()
                for _ in range(size):
                    self.slots.append(FileSlot(file_id))
            else:
                for _ in range(size):
                    self.slots.append(None)

            is_file = not is_file

    def defragment(self) -> None:
        iter_position = 0

        while iter_position < len(self.slots):
            current_slot = self.slots[iter_position]

            if current_slot is None:
                last_slot = None

                while last_slot is None:
                    last_slot = self.slots.pop(-1)

                if iter_position < len(self.slots):
                    self.slots[iter_position] = last_slot
                else:
                    self.slots.append(last_slot)

            iter_position += 1

    def calculate_checksum(self) -> int:
        checksum = 0
        for i, slot in enumerate(self.slots):
            if slot is None:
                raise RuntimeError("Slot is empty on checksum.")
            checksum += i * slot.id

        return checksum


def calculate_solution(input_values: InputType) -> int:
    register = FileRegister(input_values)
    register.defragment()
    return register.calculate_checksum()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
