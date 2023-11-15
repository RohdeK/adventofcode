
from archive.y2022.puzzles.day_12.load_inputs import input_reader
from archive.y2022.puzzles.day_12.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
    Sabqponm
    abcryxxl
    accszExk
    acctuvwj
    abdefghi
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 29
