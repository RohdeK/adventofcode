from puzzles.day_25.load_inputs import input_reader
from puzzles.day_25.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == "2=-1=0"
