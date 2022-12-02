from typing import Iterator, List, Optional

from archive.y2021.puzzles.day_11.input_part_1 import get_input


class OctoGrid:
    def __init__(self, grid_vals: List[List[int]]):
        self._grid_width = len(grid_vals[0])
        self._grid_height = len(grid_vals)

        assert all(len(line) == self._grid_width for line in grid_vals)

        self._lined_up_values = [val for line in grid_vals for val in line]

        self.flashes = 0

    def apply_steps(self, step_count: int) -> None:
        for _ in range(step_count):
            self.apply_step()

    def apply_step(self) -> None:
        self._step_init_increase_all_by_one()

        while (flashing_position := self._find_next_flash()) is not None:
            self._handle_flash(flashing_position)

    def _step_init_increase_all_by_one(self) -> None:
        for i in range(len(self._lined_up_values)):
            self._lined_up_values[i] += 1

    def _find_next_flash(self) -> Optional[int]:
        try:
            return self._lined_up_values.index(10)
        except ValueError:
            return None

    def _handle_flash(self, position: int) -> None:
        self.flashes += 1
        # Reset flashing octo
        self._lined_up_values[position] = 0

        # Handle flashing propagation
        neighbors = self._get_neighbor_positions(position)

        for index in neighbors:
            if self._lined_up_values[index] in (0, 10):
                # Either already flashed or is about to flash (cap increasing at 10)
                pass
            else:
                self._lined_up_values[index] += 1

    def _get_neighbor_positions(self, center: int) -> Iterator[int]:
        on_top_edge = center // self._grid_width == 0
        on_bottom_edge = center // self._grid_width + 1 == self._grid_height
        on_left_edge = center % self._grid_width == 0
        on_right_edge = (center + 1) % self._grid_width == 0

        # Above to the left
        if not on_left_edge and not on_top_edge:
            yield center - self._grid_width - 1

        # Above
        if not on_top_edge:
            yield center - self._grid_width

        # Above to the right
        if not on_right_edge and not on_top_edge:
            yield center - self._grid_width + 1

        # To the right
        if not on_right_edge:
            # If not on the right edge
            yield center + 1

        # Below to the right
        if not on_right_edge and not on_bottom_edge:
            yield center + self._grid_width + 1

        # Below
        if not on_bottom_edge:
            yield center + self._grid_width

        # Below to the left
        if not on_left_edge and not on_bottom_edge:
            yield center + self._grid_width - 1

        # To the left
        if not on_left_edge:
            # If not on the left edge
            yield center - 1


if __name__ == "__main__":
    grid = OctoGrid(get_input())

    grid.apply_steps(100)

    print(grid.flashes)
