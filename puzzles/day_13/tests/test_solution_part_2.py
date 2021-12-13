from puzzles.day_13.solution_part_2 import display_dots, fold_dotted_paper_full


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

    solution_dots = fold_dotted_paper_full(test_dots, test_folds)

    print(display_dots(solution_dots))
