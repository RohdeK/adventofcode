from archive.y2022.puzzles.day_18.load_inputs import input_reader
from archive.y2022.puzzles.day_18.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
    2,2,2
    1,2,2
    3,2,2
    2,1,2
    2,3,2
    2,2,1
    2,2,3
    2,2,4
    2,2,6
    1,2,5
    3,2,5
    2,1,5
    2,3,5
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 64
