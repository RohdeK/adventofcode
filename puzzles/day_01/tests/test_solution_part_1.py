from puzzles.day_01.solution_part_1 import count_increases


def test_example():
    input_values = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    test_result = count_increases(input_values)

    assert test_result == 7
