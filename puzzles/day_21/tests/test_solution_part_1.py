from puzzles.day_21.load_inputs import input_reader
from puzzles.day_21.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input, 6)

    assert solution == 16
