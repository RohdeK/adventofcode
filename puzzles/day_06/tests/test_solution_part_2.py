from puzzles.day_06.load_inputs import input_reader
from puzzles.day_06.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
    Time:      7  15   30
    Distance:  9  40  200
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 71503
