from dataclasses import dataclass
from typing import Dict, List

from archive.y2022.puzzles.day_16.load_inputs import InputType, Valve, input_reader


@dataclass
class PressureRelease:
    minutes_left: int
    release: int
    current_valve: str

    def copy(self) -> "PressureRelease":
        return PressureRelease(
            minutes_left=self.minutes_left,
            release=self.release,
            current_valve=self.current_valve,
        )


class ValveGrid:
    def __init__(self):
        self.valves: Dict[str, Valve] = {}
        self.distances: Dict[str, int] = {}
        self.max_minutes = 30
        self.minutes_per_tunnel = 1
        self.minutes_per_valve = 1
        self.starting_valve = "AA"

    def add_valve(self, valve: Valve) -> None:
        self.valves[valve.valve_name] = valve

    def calc_all_distances(self) -> None:
        for start_valve in self.valves.values():
            for next_valve in start_valve.connected_to:
                self.calculate_distances(start_valve.valve_name, next_valve)

    def calculate_distances(self, start_valve: str, current_valve: str, current_distance=0) -> None:
        registered_distance = self.get_distance(start_valve, current_valve)

        if registered_distance == 0 or registered_distance >= current_distance + 1:
            self.set_distance(start_valve, current_valve, current_distance + 1)

            for next_valve in self.valves[current_valve].connected_to:
                self.calculate_distances(start_valve, next_valve, current_distance + 1)

    def set_distance(self, valve_name_1: str, valve_name_2: str, distance: int) -> None:
        conn_name = self._to_connection_name(valve_name_1, valve_name_2)
        self.distances[conn_name] = distance

    def get_distance(self, valve_name_1: str, valve_name_2: str) -> int:
        conn_name = self._to_connection_name(valve_name_1, valve_name_2)
        return self.distances.get(conn_name, 0)

    @staticmethod
    def _to_connection_name(valve_name_1: str, valve_name_2: str) -> str:
        return "-".join(sorted([valve_name_1, valve_name_2]))

    def max_pressure_optimized(self) -> int:
        release = PressureRelease(
            minutes_left=self.max_minutes,
            current_valve=self.starting_valve,
            release=0,
        )

        worthy_valves = [valve for valve in self.valves.values() if valve.flow_rate > 0]

        return self.permutate_with_premature_end(release, worthy_valves)

    def permutate_with_premature_end(self, release: PressureRelease, next_valve_pool: List[Valve]) -> int:
        max_release = 0

        for next_valve in next_valve_pool:
            remaining_pool = next_valve_pool.copy()
            remaining_pool.remove(next_valve)
            spliced_release = release.copy()
            still_time = self.calculate_pressure_release_step(spliced_release, next_valve.valve_name)

            if still_time and len(remaining_pool) > 0:
                final_release = self.permutate_with_premature_end(spliced_release, remaining_pool)
            else:
                final_release = spliced_release.release

            if final_release > max_release:
                max_release = final_release

        return max_release

    def calculate_pressure_release_step(self, release: PressureRelease, next_valve: str) -> bool:
        distance_to_travel = self.get_distance(release.current_valve, next_valve)
        release.minutes_left -= distance_to_travel * self.minutes_per_tunnel

        release.minutes_left -= self.minutes_per_valve

        if release.minutes_left <= 0:
            return False

        valve = self.valves[next_valve]
        release.release += release.minutes_left * valve.flow_rate

        release.current_valve = next_valve

        return True


def calculate_solution(input_values: InputType) -> int:
    grid = ValveGrid()

    for valve in input_values:
        grid.add_valve(valve)

    grid.calc_all_distances()

    return grid.max_pressure_optimized()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
