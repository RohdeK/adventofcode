from puzzles.day_09.load_inputs import input_reader
from puzzles.day_09.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
    """
    """
..............
.......#XXX#..
.......X...X..
..#XXXX#...X..
..X........X..
..#XXXXXX#.X..
.........X.X..
.........#X#..
..............
"""
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 24


def test_example_2():
    raw_test_input = """
7,1
9,1
9,3
8,3
8,5
5,5
5,4
3,4
3,6
1,6
1,2
7,2
    """
    """
......#x#
#xxxxx#.x
x......##
x.#x#..X.
x.x.#xx#.
#x#......
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 18


def test_example_3():
    raw_test_input = """
7,1
9,1
9,3
8,3
8,5
3,5
3,6
1,6
1,2
7,2
    """
    """
......#x#
#xxxxx#.x
x......##
x......X.
x.#xxxx#.
#x#......
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 32


def test_example_4():
    raw_test_input = """
3,2
29,2
29,11
5,11
5,5
26,5
26,8
10,8
10,10
28,10
28,3
3,3
    """
    """
................................
..#xxxxxxxxxxxxxxxxxxxxxxxxx#...
..#xxxxxxxxxxxxxxxxxxxxxxxx#x...
...........................xx...
....#xxxxxxxxxxxxxxxxxxx#..xx...
....x...................x..xx...
....x...................x..xx...
....x....#xxxxxxxxxxxxxx#..xx...
....x....x.................xx...
....x....#xxxxxxxxxxxxxxxxx#x...
....#xxxxxxxxxxxxxxxxxxxxxxx#...
................................
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 88


def test_example_5():
    raw_test_input = """
6,1
22,1
22,2
29,2
29,10
7,10
7,9
2,9
2,7
26,7
26,4
1,4
1,2
6,2
    """
    """
.....#xxxxxxxxxxxxxxx#.......
#xxxx#...............#xxxxxx#
x...........................x
#xxxxxxxxxxxxxxxxxxxxxxxx#..x
.........................x..x
.........................x..x
.#xxxxxxxxxxxxxxxxxxxxxxx#..x
.x..........................x
.#xxxx#.....................x
......#xxxxxxxxxxxxxxxxxxxxx#
    """

    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 87


"""           z
x.............OzzzzzO
.............x.x...xz
....................z
.x..................z
O..................xz
zx..................Oz
z..................x.
zx.......x.x.........
OzzzzzzzzzO.........x

"""