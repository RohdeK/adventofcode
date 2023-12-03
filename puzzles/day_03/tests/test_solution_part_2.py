from puzzles.day_03.load_inputs import input_reader
from puzzles.day_03.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 467835
