from archive.y2021.puzzles.day_14.solution_part_2 import calculate_solution


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

    solution = calculate_solution(test_initial, test_insertions, 40)

    assert solution == 2188189693529
