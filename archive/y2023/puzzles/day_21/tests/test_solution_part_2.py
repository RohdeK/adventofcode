from puzzles.day_21.load_inputs import input_reader
from puzzles.day_21.solution_part_2 import calculate_solution


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
..........."""
    x = 0

    nlines = "\n".join(
        [
            line.replace("S", ".") * x + line + line.replace("S", ".") * x
            for line in raw_test_input.split("\n")
        ]
    )
    nlines = nlines.replace("S", ".") * x + nlines + nlines.replace("S", ".")  * x
    raw_test_input = nlines
    
    test_input = input_reader.load(raw_test_input)

    d = 4000



    #d(patch=(10, 11), inner=(6, 6)) = d((6,6), topleft) + 10 * row + 11 * col +  d(botright, d(6,6)) + 2
    # solution = calculate_solution(test_input, 6)
    #
    # assert solution == 16

    # solution = calculate_solution(test_input, 11)
    #
    # assert solution == 50

    # solution = calculate_solution(test_input, 50)

    # assert solution == 1594

    solution = calculate_solution(test_input, 100)

    assert solution == 6536

    solution = calculate_solution(test_input, 500)

    assert solution == 167004

    solution = calculate_solution(test_input, 1000)

    assert solution == 668697

    solution = calculate_solution(test_input, 5000)

    assert solution == 16733044


def test_example_2():
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

    solution = calculate_solution(test_input, 1000)

    assert solution == 668697
