import string
from typing import Dict, List, Tuple

from puzzles.day_12.load_inputs import input_reader, InputType


class HeightGrid:
    def __init__(self, heights: List[List[str]]):
        self.heights = heights
        self.distances_from_start: Dict[Tuple[int, int], int] = {}
        self.num_rows = len(heights)
        self.num_cols = len(heights[0])
        starting_points: List[Tuple[int, int]] = []

        for row_idx, row in enumerate(heights):
            for col_idx, col in enumerate(row):
                if self.is_starting_point(col):
                    starting_points.append((row_idx, col_idx))
                    self.distances_from_start[(row_idx, col_idx)] = 0
                if col == "E":
                    self.end_point = (row_idx, col_idx)

        self.run_distance_measuring(starting_points)

    @staticmethod
    def is_starting_point(height: str) -> bool:
        return height == "S"

    def get_value_from(self, dual_index: Tuple[int, int]) -> str:
        return self.heights[dual_index[0]][dual_index[1]]

    def is_mountable(self, from_height: str, to_height: str) -> bool:
        from_height_num = self.to_height_num(from_height)
        to_height_num = self.to_height_num(to_height)

        return to_height_num <= from_height_num + 1

    @staticmethod
    def to_height_num(height: str) -> int:
        if height == "S":
            height = "a"
        elif height == "E":
            height = "z"

        return string.ascii_lowercase.index(height)

    def jitter_position(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        all_pos = []

        all_pos_candidates = [
            (position[0] - 1, position[1]),
            (position[0] + 1, position[1]),
            (position[0], position[1] - 1),
            (position[0], position[1] + 1),
        ]

        for x, y in all_pos_candidates:
            if 0 <= x < self.num_rows and 0 <= y < self.num_cols:
                all_pos.append((x, y))

        return all_pos

    def run_distance_measuring(self, starting_points: List[Tuple[int, int]]) -> None:
        to_check_backlog = starting_points

        while to_check_backlog:
            current_check = to_check_backlog.pop(0)

            if current_check not in self.distances_from_start:
                continue

            current_distance = self.distances_from_start[current_check]
            current_height = self.get_value_from(current_check)

            to_check = self.jitter_position(current_check)

            for next_check in to_check:
                if next_check in self.distances_from_start:
                    continue

                next_value = self.get_value_from(next_check)

                if self.is_mountable(current_height, next_value):
                    self.distances_from_start[next_check] = current_distance + 1
                    to_check_backlog.append(next_check)

    def get_end_distance(self) -> int:
        return self.distances_from_start[self.end_point]


def calculate_solution(input_values: InputType) -> int:
    return HeightGrid(input_values).get_end_distance()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
