from typing import Tuple

from puzzles.day_09.load_inputs import input_reader, InputType


class RopeModel:
    def __init__(self, label="H"):
        self.label = label
        self.head_position = (0, 0)
        self.prev_head_position = (0, 0)
        self.tail_position = (0, 0)
        self.tail_places_visited = {self.tail_position}

    def __repr__(self):
        return f"{self.label} -- H: {self.head_position} T: {self.tail_position}"

    def on_tail_move(self) -> None:
        self.tail_places_visited.add(self.tail_position)

    def move(self, direction: str, amount: int) -> None:
        for _ in range(amount):
            self.move_one(direction)

    def move_one(self, direction: str) -> None:
        head_x, head_y = self.head_position

        if direction == "U":
            head_y += 1
        elif direction == "R":
            head_x += 1
        elif direction == "D":
            head_y -= 1
        elif direction == "L":
            head_x -= 1

        self.move_head_to((head_x, head_y))

    def move_head_to(self, position: Tuple[int, int]) -> None:
        self.prev_head_position = self.head_position

        self.head_position = position

        self.drag_tail()

    def drag_tail(self) -> None:
        x_dist = abs(self.head_position[0] - self.tail_position[0])
        y_dist = abs(self.head_position[1] - self.tail_position[1])

        if x_dist <= 1 and y_dist <= 1:
            return

        head_move_x = self.head_position[0] - self.prev_head_position[0]
        head_move_y = self.head_position[1] - self.prev_head_position[1]

        if head_move_y == 0 or head_move_x == 0:
            # Moving by horiz/vert means just follow if out of range
            self.tail_position = self.prev_head_position
        elif x_dist == 0:
            # Moved into line with diag move
            self.tail_position = self.tail_position[0], self.tail_position[1] + head_move_y
        elif y_dist == 0:
            # Moved into line with diag move
            self.tail_position = self.tail_position[0] + head_move_x, self.tail_position[1]
        else:
            # Moved away - copying the diag move
            self.tail_position = self.tail_position[0] + head_move_x, self.tail_position[1] + head_move_y

        self.on_tail_move()


def calculate_solution(input_values: InputType) -> int:
    head_tail = RopeModel()

    for direction, amount in input_values:
        head_tail.move(direction, amount)

    return len(head_tail.tail_places_visited)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
