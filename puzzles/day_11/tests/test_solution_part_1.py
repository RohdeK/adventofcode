from puzzles.day_11.load_inputs import input_reader
from puzzles.day_11.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
125 17
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input, 1)

    assert solution == 3

    solution = calculate_solution(test_input, 2)

    assert solution == 4

    solution = calculate_solution(test_input, 3)

    assert solution == 5

    solution = calculate_solution(test_input, 4)

    assert solution == 9

    solution = calculate_solution(test_input, 5)

    assert solution == 13

    solution = calculate_solution(test_input, 6)

    assert solution == 22

    solution = calculate_solution(test_input, 25)

    assert solution == 55312
