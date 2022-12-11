from puzzles.day_09.load_inputs import input_reader
from puzzles.day_09.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
    R 4
    U 4
    L 3
    D 1
    R 4
    D 1
    L 5
    R 2
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 13