from archive.y2023.puzzles.day_16.load_inputs import input_reader
from archive.y2023.puzzles.day_16.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 51
