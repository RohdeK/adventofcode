from archive.y2024.puzzles.day_10.load_inputs import input_reader
from archive.y2024.puzzles.day_10.solution_part_2 import calculate_solution


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

    assert solution == 81
