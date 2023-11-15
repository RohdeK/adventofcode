from archive.y2022.puzzles.day_24.load_inputs import input_reader
from archive.y2022.puzzles.day_24.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 18
