from archive.y2023.puzzles.day_08.load_inputs import input_reader
from archive.y2023.puzzles.day_08.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
    LR

    11A = (11B, XXX)
    11B = (XXX, 11Z)
    11Z = (11B, XXX)
    22A = (22B, XXX)
    22B = (22C, 22C)
    22C = (22Z, 22Z)
    22Z = (22B, 22B)
    XXX = (XXX, XXX)
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 6
