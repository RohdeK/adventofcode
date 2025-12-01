from puzzles.day_07.load_inputs import input_reader
from puzzles.day_07.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 3749
