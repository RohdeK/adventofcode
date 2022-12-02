from archive.y2021.puzzles.day_10.solution_part_2 import Status, calculate_score, calculate_solution, check_status


def test_example():
    test_input = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]

    solution = calculate_solution(test_input)

    assert solution == 288957


def test_check_status():
    test_input = [
        ("[({(<(())[]>[[{[]{<()<>>", Status.INCOMPLETE),
        ("[(()[<>])]({[<{<<[]>>(", Status.INCOMPLETE),
        ("{([(<{}[<>[]}>{[]{[(<()>", Status.FAULTY),
        ("(((({<>}<{<{<>}{[]{[]{}", Status.INCOMPLETE),
        ("[[<[([]))<([[{}[[()]]]", Status.FAULTY),
        ("[{[{({}]{}}([{[{{{}}([]", Status.FAULTY),
        ("{<[[]]>}<{[{[{[]{()[[[]", Status.INCOMPLETE),
        ("[<(<(<(<{}))><([]([]()", Status.FAULTY),
        ("<{([([[(<>()){}]>(<<{{", Status.FAULTY),
        ("<{([{{}}[<[[[<>{}]]]>[]]", Status.INCOMPLETE),
    ]

    for input_line, expected in test_input:
        assert check_status(input_line) == expected, input_line


def test_calculate_score():
    assert calculate_score("}}]])})]") == 288957
    assert calculate_score(")}>]})") == 5566
    assert calculate_score("}}>}>))))") == 1480781
    assert calculate_score("]]}}]}]}>") == 995444
    assert calculate_score("])}>") == 294
