
from puzzles.day_14.load_inputs import input_reader
from puzzles.day_14.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
    498,4 -> 498,6 -> 496,6
    503,4 -> 502,4 -> 502,9 -> 494,9
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 93
