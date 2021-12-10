from puzzles.day_03.solution_part_2 import calculate_co2_rate, calculate_oxygen_rate


def test_example():
    binary_report = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]

    oxy_rate = calculate_oxygen_rate(binary_report)
    co2_rate = calculate_co2_rate(binary_report)

    assert oxy_rate == 23
    assert co2_rate == 10
