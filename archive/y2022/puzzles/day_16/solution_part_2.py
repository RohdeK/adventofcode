from typing import Iterator, Tuple

from archive.y2022.puzzles.day_16.load_inputs import input_reader, InputType
from archive.y2022.puzzles.day_16.solution_part_1 import PressureRelease, ValveGrid


class ElephantValveGrid(ValveGrid):
    def max_pressure_dual(self) -> int:
        release = PressureRelease(
            minutes_left=self.max_minutes - 4,
            current_valve=self.starting_valve,
            release=0,
        )

        worthy_valves = [valve for valve in self.valves.values() if valve.flow_rate > 0]

        pressure_release = 0

        for self_partition, elef_partition in self.distribute_valves(worthy_valves):
            self_release = self.permutate_with_premature_end(release, self_partition)
            elef_release = self.permutate_with_premature_end(release, elef_partition)

            if self_release + elef_release > pressure_release:
                pressure_release = self_release + elef_release

        return pressure_release

    @staticmethod
    def distribute_valves(valves: list) -> Iterator[Tuple[list, list]]:
        for i in range(1, 2 ** len(valves)):
            i_bin = format(i, f"0{len(valves)}b")
            left_bin = []
            right_bin = []

            for index, bit in enumerate(i_bin):
                if bit == "0":
                    left_bin.append(valves[index])
                else:
                    right_bin.append(valves[index])

            yield left_bin, right_bin


def calculate_solution(input_values: InputType) -> int:
    grid = ElephantValveGrid()

    for valve in input_values:
        grid.add_valve(valve)

    grid.calc_all_distances()

    return grid.max_pressure_dual()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    # Note that this runs forever even though a best solution can be found somewhat quick.
    print(calculate_solution(puzzle_input))
