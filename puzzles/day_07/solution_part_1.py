from puzzles.day_07.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import PlanarMap


class SplitterMap(PlanarMap):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.splits = 0
        self.sources = [self.get_one_by_type("S")]

    def next(self) -> None:
        next_sources = []

        for s in self.sources:
            next_down = self.get_location_south(s)

            if not next_down:
                continue

            if next_down.type == "^":
                self.splits += 1

                split_left = self.get_location_west(next_down)
                if split_left:
                    next_sources.append(split_left)

                split_right = self.get_location_east(next_down)
                if split_right:
                    next_sources.append(split_right)
            else:
                self.change_type(next_down, "|")
                next_sources.append(next_down)

        next_sources_dedup = {loc.position: loc for loc in next_sources}
        self.sources = list(next_sources_dedup.values())

    def run(self) -> None:
        while self.sources:
            self.next()
            print(self)


def calculate_solution(input_values: InputType) -> int:
    splitter = SplitterMap(input_values)
    splitter.run()

    return splitter.splits


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
