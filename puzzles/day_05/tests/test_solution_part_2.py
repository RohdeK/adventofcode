from puzzles.day_05.load_inputs import input_reader
from puzzles.day_05.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 14
