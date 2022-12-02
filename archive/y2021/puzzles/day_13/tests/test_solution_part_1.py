from archive.y2021.puzzles.day_13.solution_part_1 import fold_dotted_paper


def test_example():
    test_dots = [
        (6, 10),
        (0, 14),
        (9, 10),
        (0, 3),
        (10, 4),
        (4, 11),
        (6, 0),
        (6, 12),
        (4, 1),
        (0, 13),
        (10, 12),
        (3, 4),
        (3, 0),
        (8, 4),
        (1, 10),
        (2, 14),
        (8, 10),
        (9, 0),
    ]

    test_folds = [(0, 7), (5, 0)]

    solution_dots = fold_dotted_paper(test_dots, test_folds[0])

    assert len(solution_dots) == 17
