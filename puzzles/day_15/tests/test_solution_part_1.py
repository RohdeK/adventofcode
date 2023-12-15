from puzzles.day_15.load_inputs import input_reader
from puzzles.day_15.solution_part_1 import calculate_solution, hash_string


def test_hash():
    assert hash_string("HASH") == 52


def test_example():
    raw_test_input = """
    rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 1320
