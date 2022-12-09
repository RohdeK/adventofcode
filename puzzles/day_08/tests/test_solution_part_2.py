from puzzles.day_08.load_inputs import input_reader
from puzzles.day_08.solution_part_2 import calculate_solution


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

    assert solution == 1


def test_larger_example():
    raw_test_input = """
    R 5
    U 8
    L 8
    D 3
    R 17
    D 10
    L 25
    U 20
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 36



