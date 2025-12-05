from archive.y2024.puzzles.day_02.load_inputs import input_reader
from archive.y2024.puzzles.day_02.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 4
