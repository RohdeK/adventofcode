from ast import literal_eval
from typing import List, Optional

from puzzles.day_10.input_part_1 import get_input


def interpret_with_replacement(input_line: str, smaller_sign: str, larger_sign: str) -> Optional[str]:
    replacements = {
        ")": "),",
        "}": "},",
        "]": "],",
        "<": smaller_sign,
        ">": larger_sign + ",",
    }

    for key, value in replacements.items():
        input_line = input_line.replace(key, value)

    try:
        literal_eval(input_line)
    except SyntaxError as ex:
        if ex.msg == "unexpected EOF while parsing":
            pass
        elif ex.msg.startswith("closing parenthesis"):
            return ex.text[ex.offset - 1]
        else:
            raise ex

    return None


def find_first_faulty_bracket(input_line: str) -> Optional[str]:
    with_parenthesis = interpret_with_replacement(input_line, "(", ")")
    with_braces = interpret_with_replacement(input_line, "{", "}")
    with_bracket = interpret_with_replacement(input_line, "[", "]")

    if with_bracket == with_braces == with_parenthesis:
        return with_bracket
    elif with_bracket == with_braces:
        return with_bracket
    elif with_bracket == with_parenthesis:
        return with_bracket
    elif with_braces == with_parenthesis:
        return with_braces  #
    else:
        return ">"


def calculate_solution(input_values: List[str]) -> int:
    check_sum = 0

    weights = {")": 3, "]": 57, "}": 1197, ">": 25137}

    for line in input_values:
        if culprit := find_first_faulty_bracket(line):
            check_sum += weights[culprit]

    return check_sum


if __name__ == "__main__":
    print(calculate_solution(get_input()))
