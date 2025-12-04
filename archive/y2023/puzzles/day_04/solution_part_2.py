from collections import defaultdict
from typing import Dict

from archive.y2023.puzzles.day_04.load_inputs import input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    card_copies: Dict[int, int] = defaultdict(lambda: 0)

    for card_index, (winning_nums, elf_nums) in enumerate(input_values):
        matches = [n for n in elf_nums if n in winning_nums]

        for i in range(card_index + 1, card_index + len(matches) + 1):
            card_copies[i] += 1 + card_copies[card_index]

    return len(input_values) + sum(card_copies.values())


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
