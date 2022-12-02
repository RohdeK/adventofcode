from archive.y2021.puzzles.day_03.load_inputs import transform_input
from archive.y2021.puzzles.day_03.solution_part_2 import calculate_co2_rate, calculate_oxygen_rate


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

    oxy_rate = calculate_oxygen_rate(binary_report)
    co2_rate = calculate_co2_rate(binary_report)

    assert oxy_rate == 23
    assert co2_rate == 10
