from typing import List, Tuple

from archive.y2021.puzzles.day_19.input_part_1 import get_input
from archive.y2021.puzzles.day_19.solution_part_1 import merge_until_done


def calculate_solution(input_values: List[List[Tuple[int, int, int]]]) -> int:
    final = merge_until_done(input_values)
    max_distance = 0

    for i in range(len(final.scanners) - 1):
        for j in range(1, len(final.scanners)):
            scanner_distance = sum((abs(val) for val in final.scanners[i] - final.scanners[j]))

            if scanner_distance > max_distance:
                max_distance = scanner_distance

    return max_distance


if __name__ == "__main__":
    print(calculate_solution(get_input()))
