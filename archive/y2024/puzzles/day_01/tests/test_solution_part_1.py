from archive.y2024.puzzles.day_01.load_inputs import input_reader
from archive.y2024.puzzles.day_01.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
3   4
4   3
2   5
1   3
3   9
3   3
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 11
