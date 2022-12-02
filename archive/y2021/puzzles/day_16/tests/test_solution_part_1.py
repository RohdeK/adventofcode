from archive.y2021.puzzles.day_16.solution_part_1 import calculate_solution


def test_example():
    assert calculate_solution("8A004A801A8002F478") == 16

    assert calculate_solution("620080001611562C8802118E34") == 12

    assert calculate_solution("C0015000016115A2E0802F182340") == 23

    assert calculate_solution("A0016C880162017C3686B18A3D4780") == 31
