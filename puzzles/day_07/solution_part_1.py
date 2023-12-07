from enum import Enum

from puzzles.day_07.load_inputs import input_reader, InputType


class HandType(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


class Hand:
    alpha = {
        "2": "A",
        "3": "B",
        "4": "C",
        "5": "D",
        "6": "E",
        "7": "F",
        "8": "G",
        "9": "H",
        "T": "I",
        "J": "J",
        "Q": "K",
        "K": "L",
        "A": "M",
    }

    def __init__(self, hand: str):
        self.hand = self.normalize(hand)
        self.type = self.get_type(hand)

    @staticmethod
    def get_type(hand: str) -> HandType:
        counts = {
            c: hand.count(c) for c in set(hand)
        }
        max_count = max(ct for ct in counts.values())

        if max_count == 5:
            return HandType.FIVE_OF_A_KIND
        elif max_count == 4:
            return HandType.FOUR_OF_A_KIND
        elif max_count == 3:
            if any(ct == 2 for ct in counts.values()):
                return HandType.FULL_HOUSE
            else:
                return HandType.THREE_OF_A_KIND
        elif max_count == 2:
            if sum(ct == 2 for ct in counts.values()) == 2:
                return HandType.TWO_PAIR
            else:
                return HandType.ONE_PAIR
        else:
            return HandType.HIGH_CARD

    def normalize(self, hand: str) -> str:
        return "".join(self.alpha[x] for x in hand)

    @property
    def as_sortable(self) -> str:
        return str(self.type.value) + self.hand


def calculate_solution(input_values: InputType) -> int:
    hands_bids = [(Hand(h), int(b)) for h, b in input_values]
    hands_bids.sort(key=lambda x: x[0].as_sortable)

    total_score = 0

    for rank, (_, bid) in enumerate(hands_bids):
        total_score += (rank + 1) * bid

    return total_score


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
