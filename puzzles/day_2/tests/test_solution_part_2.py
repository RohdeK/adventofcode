from puzzles.day_2.solution_part_2 import calculate_course


def test_example():
    input_values = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

    final_position = calculate_course((0, 0, 0), input_values)

    assert final_position == (15, 60)
