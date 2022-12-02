from archive.y2021.puzzles.day_14.solution_part_1 import apply_sequence, calculate_solution


def test_example():
    test_initial = "NNCB"

    test_insertions = [
        "CH -> B",
        "HH -> N",
        "CB -> H",
        "NH -> C",
        "HB -> C",
        "HC -> B",
        "HN -> C",
        "NN -> C",
        "BH -> H",
        "NC -> B",
        "NB -> B",
        "BN -> B",
        "BB -> N",
        "BC -> B",
        "CC -> N",
        "CN -> C",
    ]

    assert apply_sequence(test_initial, test_insertions, 1) == "NCNBCHB"
    assert apply_sequence(test_initial, test_insertions, 2) == "NBCCNBBBCBHCB"
    assert apply_sequence(test_initial, test_insertions, 3) == "NBBBCNCCNBBNBNBBCHBHHBCHB"
    assert apply_sequence(test_initial, test_insertions, 4) == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"

    solution = calculate_solution(test_initial, test_insertions, 10)

    assert solution == 1588
