from archive.y2021.puzzles.day_03.load_inputs import transform_input
from archive.y2021.puzzles.day_03.solution_part_1 import calculate_rates


def test_example():
    raw_test_input = """
    00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010
    """

    binary_report = transform_input(raw_test_input)

    gamma_rate, epsilon_rate = calculate_rates(binary_report)

    assert gamma_rate == 22
    assert epsilon_rate == 9
