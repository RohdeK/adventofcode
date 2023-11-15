from archive.y2022.puzzles.day_01.load_inputs import input_reader
from archive.y2022.puzzles.day_01.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
    1000
    2000
    3000
    
    4000
    
    5000
    6000
    
    7000
    8000
    9000
    
    10000
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 24000
