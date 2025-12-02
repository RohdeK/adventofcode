from puzzles.day_02.load_inputs import input_reader
from puzzles.day_02.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 1227775554
