from collections import defaultdict, deque
from typing import Deque, Dict, List, Tuple

from puzzles.day_15.load_inputs import input_reader, InputType
from puzzles.day_15.solution_part_1 import hash_string


class BoxCollection:
    def __init__(self):
        self.boxes: Dict[int, Tuple[List[str], List[int]]] = defaultdict(lambda: ([], []))

    def remove_label(self, label: str) -> None:
        target_box = hash_string(label)
        labels, lenses = self.boxes[target_box]

        if label in labels:
            index = labels.index(label)
            labels.pop(index)
            lenses.pop(index)

    def add_lense(self, label: str, lense: int) -> None:
        target_box = hash_string(label)
        labels, lenses = self.boxes[target_box]

        if label in labels:
            index = labels.index(label)
            lenses[index] = lense
        else:
            labels.append(label)
            lenses.append(lense)

    def focusing_power(self) -> int:
        check_sum = 0

        for box_index, (labels, lenses) in self.boxes.items():
            for lense_index, lense in enumerate(lenses):
                power = box_index + 1
                power *= lense_index + 1
                power *= lense

                check_sum += power

        return check_sum


def calculate_solution(input_values: InputType) -> int:
    boxes = BoxCollection()

    for seq in input_values:
        if seq.endswith("-"):
            boxes.remove_label(seq[:-1])
        elif "=" in seq:
            label, lense = seq.split("=")
            boxes.add_lense(label, int(lense))

    return boxes.focusing_power()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
