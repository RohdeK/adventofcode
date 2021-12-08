from puzzles.day_6.solution_part_1 import Fish, Sea


def test_example():
    fish_timers = [3, 4, 3, 1, 2]
    initial_fishes = [Fish(timer) for timer in fish_timers]

    sea = Sea()
    sea.throw_in(initial_fishes)

    assert sea.count_fishes() == 5

    sea.pass_days(18)

    assert sea.count_fishes() == 26

    sea.pass_days(80 - 18)

    assert sea.count_fishes() == 5934
