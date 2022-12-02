from archive.y2021.puzzles.day_02.load_inputs import transform_input
from archive.y2021.puzzles.day_02.solution_part_2 import calculate_course


def test_example():
    raw_test_input = """
    forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2
    """

    test_input = transform_input(raw_test_input)

    final_position = calculate_course((0, 0, 0), test_input)

    assert final_position == (15, 60)
