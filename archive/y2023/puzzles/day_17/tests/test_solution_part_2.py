from puzzles.day_17.load_inputs import input_reader
from puzzles.day_17.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == NotImplemented
