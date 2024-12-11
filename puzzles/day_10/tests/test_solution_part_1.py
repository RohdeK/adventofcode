from puzzles.day_10.load_inputs import input_reader
from puzzles.day_10.solution_part_1 import calculate_solution


def test_small_example_1():
    raw_test_input = """
...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 2


def test_small_example_2():
    raw_test_input = """
..90..9
...1.98
...2..7
6543456
765.987
876....
987....
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 4


def test_small_example_3():
    raw_test_input = """
10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 3


def test_example():
    raw_test_input = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 36
