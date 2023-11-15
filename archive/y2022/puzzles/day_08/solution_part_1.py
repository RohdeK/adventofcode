from typing import Iterator, Tuple

from archive.y2022.puzzles.day_08.load_inputs import input_reader, InputType


class Grid:
    def __init__(self, grid_vals: InputType):
        self.grid = grid_vals
        self.row_length = len(grid_vals[0])
        self.col_length = len(grid_vals)

    def get(self, row_idx: int, col_idx: int) -> int:
        return self.grid[row_idx][col_idx]

    def count_visible(self) -> int:
        visible_count = 0

        for row_idx in range(self.row_length):
            for col_idx in range(self.col_length):
                if self.is_visible(row_idx, col_idx):
                    visible_count += 1

        return visible_count

    def is_visible(self, row_idx: int, col_idx: int) -> bool:
        return self.is_visible_helper(self.top_iterator(row_idx, col_idx)) or \
            self.is_visible_helper(self.bot_iterator(row_idx, col_idx)) or \
            self.is_visible_helper(self.left_iterator(row_idx, col_idx)) or \
            self.is_visible_helper(self.right_iterator(row_idx, col_idx))

    def is_visible_helper(self, tree_iterator: Iterator[Tuple[int, int]]) -> bool:
        start_row, start_col = next(tree_iterator)

        current_height = self.get(start_row, start_col)

        for next_row, next_col in tree_iterator:
            next_height = self.get(next_row, next_col)

            if next_height < current_height:
                pass
            else:
                return False

        return True

    @staticmethod
    def top_iterator(row_idx: int, col_idx: int) -> bool:
        return ((moving_row, col_idx) for moving_row in range(row_idx, -1, -1))

    def bot_iterator(self, row_idx: int, col_idx: int) -> bool:
        return ((moving_row, col_idx) for moving_row in range(row_idx, self.row_length))

    @staticmethod
    def left_iterator(row_idx: int, col_idx: int) -> bool:
        return ((row_idx, moving_col) for moving_col in range(col_idx, -1, -1))

    def right_iterator(self, row_idx: int, col_idx: int) -> bool:
        return ((row_idx, moving_col) for moving_col in range(col_idx, self.col_length))


def calculate_solution(input_values: InputType) -> int:
    grid = Grid(input_values)

    return grid.count_visible()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
