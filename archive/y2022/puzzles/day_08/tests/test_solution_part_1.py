
from archive.y2022.puzzles.day_08.load_inputs import input_reader
from archive.y2022.puzzles.day_08.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
    30373
    25512
    65332
    33549
    35390
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 21
