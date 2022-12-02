from collections import defaultdict
from typing import Dict, Iterator, List, Tuple

from archive.y2021.puzzles.day_05.load_inputs import get_input, InputType

Point = Tuple[int, int]


class Line:
    def __init__(self, line_notation: str):
        values = [int(coord) for point in line_notation.split("->") for coord in point.split(",")]

        self._starting_point: Point = (values[0], values[1])
        self._end_point: Point = (values[2], values[3])

    def is_horizontal(self) -> bool:
        return self._starting_point[1] == self._end_point[1]

    def is_vertical(self) -> bool:
        return self._starting_point[0] == self._end_point[0]

    def points(self) -> List[Point]:
        if self.is_horizontal():

            iterator = self._including_iterator(self._starting_point[0], self._end_point[0])
            return [(i, self._starting_point[1]) for i in iterator]

        elif self.is_vertical():

            iterator = self._including_iterator(self._starting_point[1], self._end_point[1])
            return [(self._starting_point[0], i) for i in iterator]

        else:
            raise NotImplemented()

    @staticmethod
    def _including_iterator(start: int, finish: int) -> Iterator[int]:
        increasing = finish > start
        return range(start, finish + 1) if increasing else range(start, finish - 1, -1)


class OverlapGrid:
    def __init__(self):
        self._overlap_array: Dict[Point, int] = defaultdict(int)

    def register(self, line: Line) -> None:
        for point in line.points():
            self._overlap_array[point] += 1

    def points_with_overlap_at_least(self, threshold: int) -> List[Point]:
        points: List[Point] = []

        for point, overlap in self._overlap_array.items():
            if overlap >= threshold:
                points.append(point)

        return points


def find_overlapping_areas(input_values: InputType, minimum_overlap: int):
    grid = OverlapGrid()

    for line in [Line(value) for value in input_values]:
        if line.is_vertical() or line.is_horizontal():
            grid.register(line)

    return grid.points_with_overlap_at_least(minimum_overlap)


if __name__ == "__main__":
    overlapping_points = find_overlapping_areas(get_input(), 2)

    print(len(overlapping_points))
