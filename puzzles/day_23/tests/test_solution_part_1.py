from puzzles.day_23.solution_part_1 import calculate_solution, House


def test_example():
    test_input = [
        "#############",
        "#...........#",
        "###B#C#B#D###",
        "  #A#D#C#A#  ",
        "  #########  ",
    ]

    solution = calculate_solution(test_input)

    assert solution == 12521


#
#
# A: 6 + 5 + 9 + 10 + 10 + 11  = 51
# B: 8 + 4 + 4 +5 + 6 + 6 + 7  = 400
# C: 9 + 7 + 8 + 6             = 3000
# D: 5 + 4 + 4 + 2 + 28        = 43000
# = 46451
