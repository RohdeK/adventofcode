from puzzles.day_17.load_inputs import input_reader
from puzzles.day_17.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
    """
    """
    
    <000 0>11 100 101 011 000 <000>
    
    
    
    
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 117440
