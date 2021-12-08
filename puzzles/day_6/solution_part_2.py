from collections import defaultdict
from typing import Dict, List

from puzzles.day_6.input_part_1 import get_input


class OptimizedSea:
    def __init__(self, initial_fish_timers: List[int]):
        self._fishes_by_timer: Dict[int, int] = defaultdict(int)

        for timer in initial_fish_timers:
            self._fishes_by_timer[timer] += 1

        self._reset_timer = 6
        self._spawm_timer = 8

    def _pass_day(self) -> None:
        next_day_fishes: Dict[int, int] = defaultdict(int)

        for timer, count in self._fishes_by_timer.items():
            if timer > 0:
                next_day_fishes[timer - 1] += count
            else:
                next_day_fishes[self._reset_timer] += count
                next_day_fishes[self._spawm_timer] += count

        self._fishes_by_timer = next_day_fishes

    def pass_days(self, days: int) -> None:
        for _ in range(days):
            self._pass_day()

    def count_fishes(self) -> int:
        return sum(self._fishes_by_timer.values())


if __name__ == "__main__":
    sea = OptimizedSea(get_input())

    sea.pass_days(256)

    print(sea.count_fishes())
