from archive.y2023.puzzles.day_20.load_inputs import input_reader
from archive.y2023.puzzles.day_20.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
    broadcaster -> a, b, c
    %a -> b
    %b -> c
    %c -> inv
    &inv -> a
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 32000000


def test_example_2():
    raw_test_input = """
    broadcaster -> a
    %a -> inv, con
    &inv -> b
    %b -> con
    &con -> output
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 11687500
