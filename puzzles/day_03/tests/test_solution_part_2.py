from puzzles.day_03.load_inputs import input_reader
from puzzles.day_03.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
987654321111111
811111111111119
234234234234278
818181911112111
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 3121910778619
