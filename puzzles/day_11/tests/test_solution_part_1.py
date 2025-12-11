from puzzles.day_11.load_inputs import input_reader
from puzzles.day_11.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 5
