from archive.y2021.puzzles.day_11.input_part_1 import get_input
from archive.y2021.puzzles.day_11.solution_part_1 import OctoGrid


class SyncOctoGrid(OctoGrid):
    def first_synchronous_step(self, safety_upper_bound: int = 0) -> int:
        steps = 0

        while not self._all_flashed():
            self.apply_step()
            steps += 1

            if safety_upper_bound and steps > safety_upper_bound:
                raise RuntimeError(f"Exceeded limit of {safety_upper_bound} steps.")

        return steps

    def _all_flashed(self) -> bool:
        return all(val == 0 for val in self._lined_up_values)


if __name__ == "__main__":
    grid = SyncOctoGrid(get_input())

    print(grid.first_synchronous_step(1000))
