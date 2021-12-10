from puzzles.day_07.solution_part_2 import jitter_minimize_fuel


def test_example():
    crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    fuel_cost = jitter_minimize_fuel(crabs)

    assert fuel_cost == 168
