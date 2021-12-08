from puzzles.day_1.solution_part_1 import count_increases
from puzzles.day_1.solution_part_2 import moving_sum


def test_example():
    input_values = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    with_shift = moving_sum(input_values, 3)

    assert with_shift == [607, 618, 618, 617, 647, 716, 769, 792]

    test_result = count_increases(with_shift)

    assert test_result == 5
