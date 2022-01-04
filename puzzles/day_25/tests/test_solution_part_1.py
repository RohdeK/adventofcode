from puzzles.day_25.solution_part_1 import calculate_solution


def test_example():
    test_input = [
        "v...>>.vv>",
        ".vv>>.vv..",
        ">>.>v>...v",
        ">>v>>.>.v.",
        "v>v.vv.v..",
        ">.>>..v...",
        ".vv..>.>v.",
        "v.v..>>v.v",
        "....v..v.>",
    ]

    solution = calculate_solution(test_input)

    assert solution == 58
