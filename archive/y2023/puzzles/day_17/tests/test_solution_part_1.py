from puzzles.day_17.load_inputs import input_reader
from puzzles.day_17.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
    """

    """
241..........     241..3231....   241.4323.....
..154.3535...     ..1545..3....   ..154..535...
....245..42..     ........542..   .........42..
..........45.     ..........4..   ..........4..
...........3.     ..........53.   ..........53.
...........5.     ...........5.   ...........54
...........66     ...........6.   ............6
............3     ...........53   ............3
............7     ............7   ...........87
...........53     ............3   ...........53
...........6.     ...........63   ............3
...........3.     ...........3.   ............5
...........33     ...........33   ............3
"""

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 102