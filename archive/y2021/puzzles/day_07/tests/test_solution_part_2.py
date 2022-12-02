from archive.y2021.puzzles.day_07.load_inputs import transform_input
from archive.y2021.puzzles.day_07.solution_part_2 import jitter_minimize_fuel


def test_example():
    raw_test_input = """16,1,2,0,4,2,7,1,2,14"""

    crabs = transform_input(raw_test_input)

    fuel_cost = jitter_minimize_fuel(crabs)

    assert fuel_cost == 168
