from puzzles.day_06.solution_part_2 import OptimizedSea


def test_example():
    fish_timers = [3, 4, 3, 1, 2]

    sea = OptimizedSea(fish_timers)

    assert sea.count_fishes() == 5

    sea.pass_days(18)

    assert sea.count_fishes() == 26

    sea.pass_days(80 - 18)

    assert sea.count_fishes() == 5934

    sea.pass_days(256 - 80)

    assert sea.count_fishes() == 26984457539
