from typing import List

from puzzles.day_05.input_part_1 import get_input
from puzzles.day_05.solution_part_1 import Line as HorVertLine, OverlapGrid, Point


class Line(HorVertLine):
    def is_diagonal(self):
        return abs(self._starting_point[0] - self._end_point[0]) == abs(self._starting_point[1] - self._end_point[1])

    def points(self) -> List[Point]:
        if self.is_diagonal():
            x_iterator = self._including_iterator(self._starting_point[0], self._end_point[0])
            y_iterator = self._including_iterator(self._starting_point[1], self._end_point[1])
            return list(zip(x_iterator, y_iterator))

        else:
            return super().points()


def find_overlapping_areas(input_values: List[str], minimum_overlap: int):
    grid = OverlapGrid()

    for line in [Line(value) for value in input_values]:
        if line.is_vertical() or line.is_horizontal() or line.is_diagonal():
            grid.register(line)

    return grid.points_with_overlap_at_least(minimum_overlap)


if __name__ == "__main__":
    overlapping_points = find_overlapping_areas(get_input(), 2)

    print(len(overlapping_points))
