from archive.y2023.puzzles.day_01.load_inputs import input_reader
from archive.y2023.puzzles.day_01.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 281
