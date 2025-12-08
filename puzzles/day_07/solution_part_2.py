from collections import defaultdict

from puzzles.day_07.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import PlanarMap


class SplitterMap(PlanarMap):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.splits = 0
        self.sources = {self.get_one_by_type("S"): 1}

    def next(self) -> None:
        next_sources = defaultdict(int)

        for s, weight in self.sources.items():
            next_down = self.get_location_south(s)

            if not next_down:
                continue

            if next_down.type == "^":
                self.splits += weight

                split_left = self.get_location_west(next_down)
                if split_left:
                    next_sources[split_left] += weight

                split_right = self.get_location_east(next_down)
                if split_right:
                    next_sources[split_right] += weight
            else:
                self.change_type(next_down, "|")
                next_sources[next_down] += weight

        self.sources = next_sources

    def run(self) -> None:
        while self.sources:
            self.next()
            # print(self)


def calculate_solution(input_values: InputType) -> int:
    splitter = SplitterMap(input_values)
    splitter.run()

    return splitter.splits + 1


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
