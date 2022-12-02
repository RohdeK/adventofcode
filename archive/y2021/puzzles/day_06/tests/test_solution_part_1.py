from archive.y2021.puzzles.day_06.load_inputs import transform_input
from archive.y2021.puzzles.day_06.solution_part_1 import Fish, Sea


def test_example():
    raw_test_input = """3,4,3,1,2"""
    fish_timers = transform_input(raw_test_input)

    initial_fishes = [Fish(timer) for timer in fish_timers]

    sea = Sea()
    sea.throw_in(initial_fishes)

    assert sea.count_fishes() == 5

    sea.pass_days(18)

    assert sea.count_fishes() == 26

    sea.pass_days(80 - 18)

    assert sea.count_fishes() == 5934
