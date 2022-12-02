from collections import Counter, defaultdict
from typing import Dict, List

from archive.y2021.puzzles.day_14.input_part_1 import get_input


def calculate_solution(input_sequence: str, insert_statements: List[str], step_count: int) -> int:
    pairs: Dict[str, int] = defaultdict(int)

    # Initial loading
    for i in range(len(input_sequence) - 1):
        pairs[input_sequence[i : i + 2]] += 1

    parsed_statements: Dict[str, str] = {
        pair: insert for pair, insert in [statement.split(" -> ") for statement in insert_statements]
    }

    for i in range(step_count):
        new_pairs: Dict[str, int] = defaultdict(int)

        for trigger, insert in parsed_statements.items():

            if trigger not in pairs:
                continue

            new_pairs[trigger[0] + insert] += pairs[trigger]
            new_pairs[insert + trigger[1]] += pairs[trigger]

        pairs = new_pairs

    only_singles: Dict[str, int] = defaultdict(int)
    # In the following, only the leftmost from the initial is not counted.
    only_singles[input_sequence[0]] += 1
    # Only take right element, since that is the left element of another pair.
    for pair, count in pairs.items():
        only_singles[pair[1]] += count

    return max(only_singles.values()) - min(only_singles.values())


if __name__ == "__main__":
    initial_seq, instructions = get_input()

    print(calculate_solution(initial_seq, instructions, 40))
