from archive.y2023.puzzles.day_14.load_inputs import input_reader
from archive.y2023.puzzles.day_14.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input, 1_000_000_000)

    assert solution == 64
