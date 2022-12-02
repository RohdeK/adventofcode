from archive.y2021.puzzles.day_01.load_inputs import transform_input
from archive.y2021.puzzles.day_01.solution_part_1 import count_increases


def test_example():
    raw_test_input = """
    199
    200
    208
    210
    200
    207
    240
    269
    260
    263
    """

    test_input = transform_input(raw_test_input)

    solution = count_increases(test_input)

    assert solution == 7
