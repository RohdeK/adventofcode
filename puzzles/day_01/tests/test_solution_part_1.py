from puzzles.day_01.load_inputs import input_reader
from puzzles.day_01.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 3
