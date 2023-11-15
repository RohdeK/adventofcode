import string
from functools import reduce
from typing import List

from archive.y2022.puzzles.day_03.load_inputs import input_reader, InputType


def score_letter(letter: str) -> int:
    return ('0' + string.ascii_lowercase + string.ascii_uppercase).index(letter)


def find_shared_in_sets(contents: List[str]) -> str:
    content_sets = [set(c) for c in contents]
    common = reduce(lambda x, y: x & y, content_sets)
    return "".join(common)


def find_shared_in_compartments(content: str) -> str:
    half_length = len(content) // 2
    comp_1, comp_2 = content[:half_length], content[half_length:]
    return find_shared_in_sets([comp_1, comp_2])


def calculate_solution(input_values: InputType) -> int:
    score = 0

    for sack_content in input_values:
        shared_in_compartments = find_shared_in_compartments(sack_content)

        for letter in shared_in_compartments:
            score += score_letter(letter)

    return score


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
