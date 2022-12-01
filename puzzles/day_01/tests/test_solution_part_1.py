
from puzzles.day_01.solution_part_1 import calculate_solution


def test_example():
    test_input = [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]

    solution = calculate_solution(test_input)

    assert solution == 24000
