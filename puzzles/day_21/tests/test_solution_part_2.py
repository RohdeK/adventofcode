from puzzles.day_21.load_inputs import input_reader
from puzzles.day_21.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = """
    root: pppw + sjmn
    dbpl: 5
    cczh: sllz + lgvd
    zczc: 2
    ptdq: humn - dvpt
    dvpt: 3
    lfqf: 4
    humn: 5
    ljgn: 2
    sjmn: drzm * dbpl
    sllz: 4
    pppw: cczh / lfqf
    lgvd: ljgn * ptdq
    drzm: hmdt - zczc
    hmdt: 32
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 301
