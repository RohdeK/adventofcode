from puzzles.day_09.load_inputs import input_reader
from puzzles.day_09.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
2333133121414131402
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 2858
