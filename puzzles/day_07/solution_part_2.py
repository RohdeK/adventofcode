from puzzles.day_07.load_inputs import input_reader, InputType
from puzzles.day_07.solution_part_1 import HandType


class Hand:
    alpha = {
        "J": "A",
        "2": "B",
        "3": "C",
        "4": "D",
        "5": "E",
        "6": "F",
        "7": "G",
        "8": "H",
        "9": "J",
        "T": "K",
        "Q": "L",
        "K": "M",
        "A": "N",
    }

    def __init__(self, hand: str):
        self.hand = self.normalize(hand)
        self.type = self.get_type(hand)

    @staticmethod
    def get_type(hand: str) -> HandType:
        counts = {
            c: hand.count(c) for c in set(hand)
        }
        joker_counts = counts.pop("J", 0)
        max_count = max(ct for ct in counts.values()) if counts else 0
        max_count += joker_counts

        if max_count == 5:
            # Case with joker we have 5. Always best option.
            return HandType.FIVE_OF_A_KIND
        elif max_count == 4:
            # Case with joker we can have 4. Always superior than taking joker for sth else.
            return HandType.FOUR_OF_A_KIND
        elif max_count == 3:
            # Case we have 3 max with joker, meaning 0, 1 or 2 jokers.
            # 2 jokers and max count 3 means all others are 1
            if joker_counts == 2:
                return HandType.THREE_OF_A_KIND
            # 1 joker can mean we have either one or two more pairs
            elif joker_counts == 1:
                if sum(ct == 2 for ct in counts.values()) == 2:
                    return HandType.FULL_HOUSE
                else:
                    return HandType.THREE_OF_A_KIND
            # 0 joker means regular logic
            else:
                if any(ct == 2 for ct in counts.values()):
                    return HandType.FULL_HOUSE
                else:
                    return HandType.THREE_OF_A_KIND
        elif max_count == 2:
            # Case we have 2 max with joker means 0 or 1 jokers
            # Case 1 joker means we have no pairs otherwise making a 3 of a kind is better
            if joker_counts == 1:
                return HandType.ONE_PAIR
            # 0 joker means regular logic
            else:
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
