from archive.y2024.puzzles.day_12.load_inputs import input_reader
from archive.y2024.puzzles.day_12.solution_part_2 import calculate_solution


def test_example_1():
    raw_test_input = """
AAAA
BBCD
BBCC
EEEC
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 80


def test_example_2():
    raw_test_input = """
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 236


def test_example_3():
    raw_test_input = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 368


def test_example_4():
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

    assert solution == 1206
