from archive.y2024.puzzles.day_20.load_inputs import input_reader
from archive.y2024.puzzles.day_20.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input, 0)

    assert solution == 14 + 14 + 2 + 4 + 2 + 3 + 1 + 1 + 1 + 1 + 1
