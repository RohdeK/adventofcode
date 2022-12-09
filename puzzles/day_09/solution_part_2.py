from typing import Set, Tuple

from puzzles.day_09.load_inputs import input_reader, InputType
from puzzles.day_09.solution_part_1 import RopeModel


class ChainableRopeModel(RopeModel):
    def __init__(self, label):
        super().__init__(label=label)
        self.following_model = None

    def register_dependent(self, other: RopeModel) -> None:
        self.following_model = other

    def on_tail_move(self) -> None:
        super().on_tail_move()
        if self.following_model:
            # print(f"Moving {self.following_model.label} head to {self.tail_position}")
            self.following_model.move_head_to(self.tail_position)


class MultiRopeModel:
    def __init__(self, knot_count: int):
        self.submodels = [ChainableRopeModel(label=i or "H") for i in range(knot_count)]

        for i in range(knot_count - 1):
            following_model = self.submodels[i + 1]
            leading_model = self.submodels[i]
            leading_model.register_dependent(following_model)

    def move(self, direction: str, amount: int) -> None:
        self.submodels[0].move(direction, amount)

    def last_tail_places_visited(self) -> Set[Tuple[int, int]]:
        return self.submodels[-1].tail_places_visited


def calculate_solution(input_values: InputType) -> int:
    head_tail = MultiRopeModel(9)

    for direction, amount in input_values:
        head_tail.move(direction, amount)

    return len(head_tail.last_tail_places_visited())


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
