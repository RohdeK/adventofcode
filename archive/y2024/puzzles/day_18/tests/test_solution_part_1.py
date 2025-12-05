from archive.y2024.puzzles.day_18.load_inputs import input_reader
from archive.y2024.puzzles.day_18.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input, 12, (6, 6))

    assert solution == 22
