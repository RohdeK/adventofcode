from archive.y2024.puzzles.day_12.load_inputs import input_reader
from archive.y2024.puzzles.day_12.solution_part_1 import calculate_solution


def test_example_1():
    raw_test_input = """
AAAA
BBCD
BBCC
EEEC
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 140


def test_example_2():
    raw_test_input = """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 772


def test_example_3():
    raw_test_input = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 1930
