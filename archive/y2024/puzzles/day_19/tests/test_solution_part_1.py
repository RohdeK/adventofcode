from archive.y2024.puzzles.day_19.load_inputs import input_reader
from archive.y2024.puzzles.day_19.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 6
