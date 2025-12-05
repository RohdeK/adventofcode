from archive.y2024.puzzles.day_14.load_inputs import input_reader
from archive.y2024.puzzles.day_14.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input, (11, 7))

    assert solution == 12
