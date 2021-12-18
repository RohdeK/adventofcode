from puzzles.day_18.solution_part_1 import SnailNumber, calculate_solution


def test_magnitude():
    assert SnailNumber.from_rep([[1, 2], [[3, 4], 5]]).magnitude() == 143
    assert SnailNumber.from_rep([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]).magnitude() == 1384
    assert SnailNumber.from_rep([[[[1, 1], [2, 2]], [3, 3]], [4, 4]]).magnitude() == 445
    assert SnailNumber.from_rep([[[[3, 0], [5, 3]], [4, 4]], [5, 5]]).magnitude() == 791
    assert SnailNumber.from_rep([[[[5, 0], [7, 4]], [5, 5]], [6, 6]]).magnitude() == 1137
    assert SnailNumber.from_rep([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]).magnitude() == 3488


def test_breakdown():
    test_input = [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]
    test_number = SnailNumber.from_rep(test_input)

    test_number.breakdown()
    assert test_number.to_rep() == [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]


def test_walk_numerals():
    test_input = [[[[0, 7], 4], [15, [0, 13]]], [1, 1]]
    test_number = SnailNumber.from_rep(test_input)

    result = list(test_number.walk_numerals())

    result_vals = [val[0].to_rep() for val in result]

    assert result_vals == [[0, 7], [[0, 7], 4], [15, [0, 13]], [0, 13], [1, 1]]


def test_walk_numeral_depths():
    test_input = [[[[0, 7], 4], [15, [0, 13]]], [1, 1]]
    test_number = SnailNumber.from_rep(test_input)

    result = list(test_number.walk_numerals())

    depth_vals = [val[1] for val in result]

    assert depth_vals == [3, 2, 2, 3, 1]


def test_breakdown_split():
    test_input = [[[[0, 7], 4], [15, [0, 13]]], [1, 1]]
    test_number = SnailNumber.from_rep(test_input)

    work_done = test_number.breakdown_split()

    assert test_number.to_rep() == [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]
    assert work_done


def test_breakdown_explode():
    test_input = [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]
    test_number = SnailNumber.from_rep(test_input)

    work_done = test_number.breakdown_explode()

    assert test_number.to_rep() == [[[[0, 7], 4], [7, [[8, 4], 9]]], [1, 1]]
    assert work_done

    test_input = [[[[0, 7], 4], [7, [[8, 4], 9]]], [1, 1]]
    test_number = SnailNumber.from_rep(test_input)

    work_done = test_number.breakdown_explode()

    assert test_number.to_rep() == [[[[0, 7], 4], [15, [0, 13]]], [1, 1]]
    assert work_done


def test_example():
    test_input = [
        [[[0, [5, 8]], [[1, 7], [9, 6]]], [[4, [1, 2]], [[1, 4], 2]]],
        [[[5, [2, 8]], 4], [5, [[9, 9], 0]]],
        [6, [[[6, 2], [5, 6]], [[7, 6], [4, 7]]]],
        [[[6, [0, 7]], [0, 9]], [4, [9, [9, 0]]]],
        [[[7, [6, 4]], [3, [1, 3]]], [[[5, 5], 1], 9]],
        [[6, [[7, 3], [3, 2]]], [[[3, 8], [5, 7]], 4]],
        [[[[5, 4], [7, 7]], 8], [[8, 3], 8]],
        [[9, 3], [[9, 9], [6, [4, 9]]]],
        [[2, [[7, 7], 7]], [[5, 8], [[9, 3], [0, 2]]]],
        [[[[5, 2], 5], [8, [3, 7]]], [[5, [7, 5]], [4, 4]]],
    ]

    solution = calculate_solution(test_input)

    assert solution == 4140
