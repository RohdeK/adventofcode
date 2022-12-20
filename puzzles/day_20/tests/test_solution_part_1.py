from puzzles.day_20.load_inputs import input_reader
from puzzles.day_20.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
    1
    2
    -3
    3
    -2
    0
    4
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 3