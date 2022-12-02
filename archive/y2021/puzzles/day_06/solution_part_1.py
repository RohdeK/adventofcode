from typing import List, Optional

from archive.y2021.puzzles.day_06.load_inputs import get_input


class Fish:
    def __init__(self, init_timer: int = 8):
        self._timer = init_timer
        self._cycle = 6

    def tick(self) -> Optional["Fish"]:
        if self._timer == 0:
            self._timer = self._cycle
            return Fish()
        else:
            self._timer -= 1


class Sea:
    def __init__(self):
        self._fishes: List[Fish] = []

    def throw_in(self, fishes: List[Fish]) -> None:
        self._fishes.extend(fishes)

    def pass_days(self, days: int) -> None:
        for _ in range(days):
            for fish in tuple(self._fishes):
                if new_fish := fish.tick():
                    self._fishes.append(new_fish)

    def count_fishes(self) -> int:
        return len(self._fishes)


if __name__ == "__main__":
    initial_fishes = [Fish(timer) for timer in get_input()]

    sea = Sea()
    sea.throw_in(initial_fishes)

    sea.pass_days(80)

    print(sea.count_fishes())
