from puzzles.day_03.load_inputs import input_reader
from puzzles.day_03.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 161