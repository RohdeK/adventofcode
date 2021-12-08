from puzzles.day_8.solution_part_2 import DigitClock, calculate_output_values, deduce_output_value


def test_example():
    test_input = [
        "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
        "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
        "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
        "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
        "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
        "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
        "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
        "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
        "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
        "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
    ]

    solution = sum(calculate_output_values(test_input))

    assert solution == 61229


def test_mapping():
    test_input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

    solution = deduce_output_value(test_input)

    assert solution == 5353


def test_digit_clock():
    clock = DigitClock("d", "e", "a", "f", "g", "b", "c")

    assert clock.interpret("acedgfb") == 8
    assert clock.interpret("cdfbe") == 5
    assert clock.interpret("gcdfa") == 2
    assert clock.interpret("fbcad") == 3
    assert clock.interpret("dab") == 7
    assert clock.interpret("cefabd") == 9
    assert clock.interpret("cdfgeb") == 6
    assert clock.interpret("eafb") == 4
    assert clock.interpret("cagedb") == 0
    assert clock.interpret("ab") == 1
