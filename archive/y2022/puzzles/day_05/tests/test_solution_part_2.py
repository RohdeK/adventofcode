
from archive.y2022.puzzles.day_05.load_inputs import input_reader
from archive.y2022.puzzles.day_05.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
        [D]    
    [N] [C]    
    [Z] [M] [P]
     1   2   3 
    
    move 1 from 2 to 1
    move 3 from 1 to 3
    move 2 from 2 to 1
    move 1 from 1 to 2
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == "MCD"
