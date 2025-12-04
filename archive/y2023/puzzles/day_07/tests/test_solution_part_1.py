from archive.y2023.puzzles.day_07.load_inputs import input_reader
from archive.y2023.puzzles.day_07.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
    32T3K 765
    T55J5 684
    KK677 28
    KTJJT 220
    QQQJA 483
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 6440
