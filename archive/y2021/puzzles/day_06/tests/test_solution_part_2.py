from archive.y2021.puzzles.day_06.load_inputs import transform_input
from archive.y2021.puzzles.day_06.solution_part_2 import OptimizedSea


def test_example():
    raw_test_input = """3,4,3,1,2"""
    fish_timers = transform_input(raw_test_input)

    sea = OptimizedSea(fish_timers)

    assert sea.count_fishes() == 5

    sea.pass_days(18)

    assert sea.count_fishes() == 26

    sea.pass_days(80 - 18)

    assert sea.count_fishes() == 5934

    sea.pass_days(256 - 80)

    assert sea.count_fishes() == 26984457539
