from archive.y2021.puzzles.day_17.solution_part_1 import calculate_solution


def test_example():
    test_input = (20, 30), (-10, -5)

    solution = calculate_solution(*test_input)

    assert solution == 45
