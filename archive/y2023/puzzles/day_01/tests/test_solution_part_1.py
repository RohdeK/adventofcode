from archive.y2023.puzzles.day_01.load_inputs import input_reader
from archive.y2023.puzzles.day_01.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 142
