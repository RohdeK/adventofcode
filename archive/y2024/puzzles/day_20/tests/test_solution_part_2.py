from archive.y2024.puzzles.day_20.load_inputs import input_reader
from archive.y2024.puzzles.day_20.solution_part_2 import calculate_solution


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

    solution = calculate_solution(test_input, 50)

    assert solution == 32 + 31 + 29 + 39 + 25 + 23 + 20 + 19 + 12 + 14 + 12 + 22 + 4 + 3
