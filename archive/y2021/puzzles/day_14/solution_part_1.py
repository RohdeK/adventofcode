from collections import Counter
from typing import Dict, List

from archive.y2021.puzzles.day_14.input_part_1 import get_input


def apply_sequence(input_sequence: str, insert_statements: List[str], step_count: int) -> str:
    sequence_break_placeholder = "-"

    parsed_statements: Dict[str, str] = {
        pair: pair[0] + sequence_break_placeholder + insert + sequence_break_placeholder + pair[1]
        for pair, insert in [statement.split(" -> ") for statement in insert_statements]
    }

    for _ in range(step_count):
        for trigger, insert in parsed_statements.items():
            while trigger in input_sequence:
                input_sequence = input_sequence.replace(trigger, insert)

        input_sequence = input_sequence.replace(sequence_break_placeholder, "")

    return input_sequence


def calculate_solution(input_sequence: str, insert_statements: List[str], step_count: int) -> int:
    output_sequence = apply_sequence(input_sequence, insert_statements, step_count)

    counts = Counter(list(output_sequence)).most_common()

    return counts[0][1] - counts[-1][1]


if __name__ == "__main__":
    initial_seq, instructions = get_input()

    print(calculate_solution(initial_seq, instructions, 10))
