from puzzles.day_09.load_inputs import input_reader
from puzzles.day_09.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 50
