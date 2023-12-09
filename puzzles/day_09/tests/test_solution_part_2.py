from puzzles.day_09.load_inputs import input_reader
from puzzles.day_09.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
    0 3 6 9 12 15
    1 3 6 10 15 21
    10 13 16 21 30 45
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 2
