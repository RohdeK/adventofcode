from ast import literal_eval
from enum import Enum
from typing import List, Optional

from puzzles.day_10.input_part_1 import get_input


class Status(Enum):
    COMPLETE = 0
    INCOMPLETE = 1
    FAULTY = 2


def status_with_replacement(input_line: str, smaller_sign: str, larger_sign: str) -> Status:
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
            return Status.INCOMPLETE
        elif ex.msg.startswith("closing parenthesis"):
            return Status.FAULTY
        else:
            raise ex
    except TypeError:
        # TypeError can only happen if the syntax is correct
        pass

    return Status.COMPLETE


def check_status(input_line: str) -> Status:
    with_parenthesis = status_with_replacement(input_line, "(", ")")
    with_braces = status_with_replacement(input_line, "{", "}")
    with_bracket = status_with_replacement(input_line, "[", "]")

    if with_bracket == with_braces == with_parenthesis:
        return with_bracket
    elif with_bracket == with_braces:
        return with_bracket
    elif with_bracket == with_parenthesis:
        return with_bracket
    elif with_braces == with_parenthesis:
        return with_braces
    else:
        return Status.FAULTY


def find_completiom(input_line: str) -> Optional[str]:
    completion_sequence = ""
    should_be_completed = check_status(input_line) == Status.INCOMPLETE

    while should_be_completed:
        for br in (")", "]", "}", ">"):
            status = check_status(input_line + completion_sequence + br)

            if status == Status.COMPLETE:
                completion_sequence += br
                should_be_completed = False
                break
            elif status == Status.INCOMPLETE:
                completion_sequence += br
                should_be_completed = True
                break
            elif status == Status.FAULTY:
                continue

    return completion_sequence


def calculate_score(completion: str) -> int:
    score = 0
    weights = {")": 1, "]": 2, "}": 3, ">": 4}

    for char in list(completion):
        score *= 5
        score += weights[char]

    return score


def calculate_solution(input_values: List[str]) -> int:
    completion_payouts = []

    for line in input_values:
        if completion := find_completiom(line):
            completion_payouts.append(calculate_score(completion))

    return sorted(completion_payouts)[len(completion_payouts) // 2]


if __name__ == "__main__":
    print(calculate_solution(get_input()))
