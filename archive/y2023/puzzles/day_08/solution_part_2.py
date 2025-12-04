import math
from collections import defaultdict
from functools import reduce
from typing import Dict, Iterator

from archive.y2023.puzzles.day_08.load_inputs import Locator, input_reader, InputType


class FastForward:
    def __init__(self, from_: str, input_values: InputType):
        (self.move_pattern, ), locators = input_values
        self.locators_by_from: Dict[str, Locator] = {lc.from_: lc for lc in locators}
        self.z_locations_after = []
        self.periodicity_from = 0
        self.periodicity = 0
        self._fast_forward(from_)

    def includes(self, value: int) -> bool:
        if value in self.z_locations_after:
            return True

        if value < self.periodicity_from:
            return False

        repeated_z = [z for z in self.z_locations_after if z >= self.periodicity_from]

        relative_value = value % self.periodicity
        if relative_value == 0:
            relative_value = self.periodicity

        return relative_value in repeated_z

    def __repr__(self):
        return f"{self.z_locations_after} X {self.periodicity} ({self.periodicity_from})"

    def endless_iter(self) -> Iterator[int]:
        for z in self.z_locations_after:
            yield z

        post_period_z = [z for z in self.z_locations_after if z >= self.periodicity_from]

        period = 1

        while True:
            for z in post_period_z:
                yield z + self.periodicity * period
            period += 1

    def _direction_from(self, iteration: int) -> int:
        return {"L": 0, "R": 1}[self.move_pattern[iteration % len(self.move_pattern)]]

    def _fast_forward(self, from_: str) -> None:
        periodicity = None
        current_iteration = 0
        current_location = from_
        z_locations_after = []
        seen_locations = defaultdict(list)

        while periodicity is None:
            loc = self.locators_by_from[current_location]
            current_location = [loc.left_, loc.right_][self._direction_from(current_iteration)]
            current_iteration += 1

            if current_location in seen_locations:
                for i in seen_locations[current_location]:
                    if (current_iteration - i) % len(self.move_pattern) == 0:
                        self.z_locations_after = z_locations_after
                        self.periodicity_from = i - 1
                        self.periodicity = current_iteration - i
                        return

            seen_locations[current_location].append(current_iteration)

            if current_location.endswith("Z"):
                z_locations_after.append(current_iteration)


def lcm(a, b):
    # Pulled off the internet for least common divisor
    return abs(a*b) // math.gcd(a, b)


def calculate_solution(input_values: InputType) -> int:
    _, locators = input_values

    start_locations = [lc.from_ for lc in locators if lc.from_.endswith("A")]
    ff_starts = [FastForward(from_, input_values) for from_ in start_locations]

    # Cheated:
    # Checked and every fast forward had a single z hit in a period which was the
    # exact period size. Hence finding the common multiple of these is the solution.
    return reduce(lcm, [ff.periodicity for ff in ff_starts])


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
