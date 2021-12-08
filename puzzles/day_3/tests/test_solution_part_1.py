from puzzles.day_3.solution_part_1 import calculate_rates


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

    gamma_rate, epsilon_rate = calculate_rates(binary_report)

    assert gamma_rate == 22
    assert epsilon_rate == 9
