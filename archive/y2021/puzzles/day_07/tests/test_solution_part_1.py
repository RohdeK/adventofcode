from archive.y2021.puzzles.day_07.solution_part_1 import move_into_line


def test_example():
    crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    fuel_cost = move_into_line(crabs)

    assert fuel_cost == 37
