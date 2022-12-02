
from puzzles.day_02.load_inputs import transform_input
from puzzles.day_02.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = "A Y\nB X\nC Z\n"
    
    test_input = transform_input(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 12
