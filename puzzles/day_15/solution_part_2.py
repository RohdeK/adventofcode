from typing import List

from puzzles.day_15.input_part_1 import get_input
from puzzles.day_15.solution_part_1 import shortest_path_length


def multiply_grid(input_values: List[List[int]], size: int, increase=0) -> List[List[int]]:
    original_width = len(input_values[0])
    new_width = original_width * size
    original_height = len(input_values)
    new_height = original_height * size

    new_grid = [[0] * new_width for _ in range(new_height)]

    for i in range(new_width):
        for j in range(new_height):
            original_x = i % original_width
            steps_x = i // original_width

            original_y = j % original_height
            stepy_y = j // original_height

            original_val = input_values[original_y][original_x]

            new_val = original_val + (steps_x + stepy_y) * increase

            new_val = new_val % 9

            if new_val == 0:
                new_val = 9

            new_grid[j][i] = new_val

    assert all(all(0 < val < 10 for val in row) for row in new_grid)

    return new_grid


if __name__ == "__main__":
    input_vals = multiply_grid(get_input(), size=5, increase=1)
    print(shortest_path_length(input_vals))
