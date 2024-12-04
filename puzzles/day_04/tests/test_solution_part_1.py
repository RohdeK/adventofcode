from puzzles.day_04.load_inputs import input_reader
from puzzles.day_04.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 18
