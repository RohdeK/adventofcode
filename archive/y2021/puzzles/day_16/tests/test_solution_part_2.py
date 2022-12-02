from archive.y2021.puzzles.day_16.solution_part_2 import calculate_solution


def test_example():
    assert calculate_solution("C200B40A82") == 3

    assert calculate_solution("04005AC33890") == 54

    assert calculate_solution("880086C3E88112") == 7

    assert calculate_solution("CE00C43D881120") == 9

    assert calculate_solution("D8005AC2A8F0") == 1

    assert calculate_solution("F600BC2D8F") == 0

    assert calculate_solution("9C005AC2F8F0") == 0

    assert calculate_solution("9C0141080250320F1802104A08") == 1
