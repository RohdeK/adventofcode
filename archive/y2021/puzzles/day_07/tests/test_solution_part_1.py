from archive.y2021.puzzles.day_07.load_inputs import transform_input
from archive.y2021.puzzles.day_07.solution_part_1 import move_into_line


def test_example():
    raw_test_input = """16,1,2,0,4,2,7,1,2,14"""

    crabs = transform_input(raw_test_input)

    fuel_cost = move_into_line(crabs)

    assert fuel_cost == 37
