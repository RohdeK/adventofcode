from archive.y2021.puzzles.day_05.load_inputs import transform_input
from archive.y2021.puzzles.day_05.solution_part_1 import find_overlapping_areas


def test_example():
    raw_test_input = """
    0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2
    """

    test_input = transform_input(raw_test_input)

    overlapping_points = find_overlapping_areas(test_input, 2)

    assert len(overlapping_points) == 5
