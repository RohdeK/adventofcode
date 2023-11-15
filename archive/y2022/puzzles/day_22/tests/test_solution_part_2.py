from archive.y2022.puzzles.day_22.load_inputs import input_reader
from archive.y2022.puzzles.day_22.solution_part_1 import Direction
from archive.y2022.puzzles.day_22.solution_part_2 import calculate_solution


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

    facets = [
        [None, None, 1],
        [5, 4, 2],
        [None, None, 6, 3],
    ]

    facet_movements = {
        1: {
            Direction.UP: (5, 2),
            Direction.DOWN: (2, 0),
            Direction.LEFT: (4, 3),
            Direction.RIGHT: (3, 2),
        },
        2: {
            Direction.UP: (1, 0),
            Direction.DOWN: (6, 0),
            Direction.LEFT: (4, 0),
            Direction.RIGHT: (3, 1),
        },
        3: {
            Direction.UP: (2, 3),
            Direction.DOWN: (5, 3),
            Direction.LEFT: (6, 0),
            Direction.RIGHT: (1, 2),
        },
        4: {
            Direction.UP: (1, 1),
            Direction.DOWN: (6, 3),
            Direction.LEFT: (5, 0),
            Direction.RIGHT: (2, 0),
        },
        5: {
            Direction.UP: (1, 2),
            Direction.DOWN: (6, 2),
            Direction.LEFT: (3, 1),
            Direction.RIGHT: (4, 0),
        },
        6: {
            Direction.UP: (2, 0),
            Direction.DOWN: (5, 2),
            Direction.LEFT: (4, 1),
            Direction.RIGHT: (3, 0),
        }
    }

    solution = calculate_solution(test_input, facets, facet_movements, 4)

    assert solution == 5031
