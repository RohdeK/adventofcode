from archive.y2021.puzzles.day_01.load_inputs import transform_input
from archive.y2021.puzzles.day_01.solution_part_1 import count_increases
from archive.y2021.puzzles.day_01.solution_part_2 import moving_sum


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

    with_shift = moving_sum(test_input, 3)

    assert with_shift == [607, 618, 618, 617, 647, 716, 769, 792]

    solution = count_increases(with_shift)

    assert solution == 5
