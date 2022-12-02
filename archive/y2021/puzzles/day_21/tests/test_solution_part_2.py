from archive.y2021.puzzles.day_21.solution_part_2 import calculate_solution


def test_example():
    test_input = [4, 8]

    solution = calculate_solution(test_input)

    assert solution == 444356092776315
