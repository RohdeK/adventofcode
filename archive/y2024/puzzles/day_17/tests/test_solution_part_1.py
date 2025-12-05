from archive.y2024.puzzles.day_17.load_inputs import input_reader
from archive.y2024.puzzles.day_17.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
    """
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == "4,6,3,5,6,3,5,2,1,0"
