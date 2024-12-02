from puzzles.day_11.load_inputs import input_reader
from puzzles.day_11.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input, 1)

    assert solution == 374

    solution = calculate_solution(test_input, 9)

    assert solution == 1030

    solution = calculate_solution(test_input, 99)

    assert solution == 8410
