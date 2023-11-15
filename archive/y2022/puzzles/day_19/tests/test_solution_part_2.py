from archive.y2022.puzzles.day_19.load_inputs import input_reader
from archive.y2022.puzzles.day_19.solution_part_2 import get_score


def test_example():
    raw_test_input = """
    Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
    Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = get_score(test_input[0])

    assert solution == 56

    solution = get_score(test_input[1])

    assert solution == 62
