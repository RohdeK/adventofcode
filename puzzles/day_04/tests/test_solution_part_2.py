from puzzles.day_04.load_inputs import input_reader
from puzzles.day_04.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
    2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 4
