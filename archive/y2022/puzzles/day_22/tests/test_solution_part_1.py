from archive.y2022.puzzles.day_22.load_inputs import input_reader
from archive.y2022.puzzles.day_22.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 6032
