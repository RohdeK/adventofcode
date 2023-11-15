from typing import Iterator, Tuple

from archive.y2022.puzzles.day_08.load_inputs import input_reader, InputType
from archive.y2022.puzzles.day_08.solution_part_1 import Grid


class ScenicGrid(Grid):
    def scenic_score_helper(self, tree_iterator: Iterator[Tuple[int, int]]) -> int:
        start_row, start_col = next(tree_iterator)
        directional_score = 0

        current_height = self.get(start_row, start_col)

        for next_row, next_col in tree_iterator:
            directional_score += 1
            next_height = self.get(next_row, next_col)

            if next_height >= current_height:
                break

        return directional_score

    def scenic_score(self, row_idx: int, col_idx: int) -> int:
        top_score = self.scenic_score_helper(self.top_iterator(row_idx, col_idx))
        bot_score = self.scenic_score_helper(self.bot_iterator(row_idx, col_idx))
        left_score = self.scenic_score_helper(self.left_iterator(row_idx, col_idx))
        right_score = self.scenic_score_helper(self.right_iterator(row_idx, col_idx))

        return top_score * bot_score * left_score * right_score

    def max_scenic_score(self) -> int:
        max_score = 0

        for row_idx in range(self.row_length):
            for col_idx in range(self.col_length):
                iter_score = self.scenic_score(row_idx, col_idx)

                if iter_score > max_score:
                    max_score = iter_score

        return max_score


def calculate_solution(input_values: InputType) -> int:
    grid = ScenicGrid(input_values)
    return grid.max_scenic_score()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
