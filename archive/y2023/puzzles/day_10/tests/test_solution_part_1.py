from archive.y2023.puzzles.day_10.load_inputs import input_reader
from archive.y2023.puzzles.day_10.solution_part_1 import calculate_solution


def test_example_1():
    raw_test_input = """
.....
.S-7.
.|.|.
.L-J.
.....
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 4


def test_example_2():
    raw_test_input = """
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 4


def test_example_3():
    raw_test_input = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 8


def test_example_4():
    raw_test_input = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 8
