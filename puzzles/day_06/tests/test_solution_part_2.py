from puzzles.day_06.load_inputs import input_reader
from puzzles.day_06.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 3263827
