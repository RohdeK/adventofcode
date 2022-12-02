from archive.y2021.puzzles.day_12.solution_part_2 import count_all_paths


def test_example():
    test_input = [
        "start-A",
        "start-b",
        "A-c",
        "A-b",
        "b-d",
        "A-end",
        "b-end",
    ]

    solution = count_all_paths(test_input)

    assert solution == 36
