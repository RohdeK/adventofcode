from collections import Counter
from typing import List

from puzzles.day_08.input_part_1 import get_input


class DigitClock:
    def __init__(self, u: str, lu: str, ru: str, m: str, ll: str, rl: str, l: str):
        assert all([u, lu, ru, m, ll, rl, l])
        assert len({u, lu, ru, m, ll, rl, l}) == 7

        self._reps = {
            self._normalize(f"{u}{ru}{rl}{l}{ll}{lu}"): 0,
            self._normalize(f"{ru}{rl}"): 1,
            self._normalize(f"{u}{ru}{m}{ll}{l}"): 2,
            self._normalize(f"{u}{ru}{m}{rl}{l}"): 3,
            self._normalize(f"{ru}{m}{lu}{rl}"): 4,
            self._normalize(f"{u}{lu}{m}{rl}{l}"): 5,
            self._normalize(f"{u}{lu}{m}{ll}{rl}{l}"): 6,
            self._normalize(f"{u}{ru}{rl}"): 7,
            self._normalize(f"{u}{ru}{lu}{m}{ll}{rl}{l}"): 8,
            self._normalize(f"{u}{ru}{lu}{m}{rl}{l}"): 9,
        }

    def interpret(self, digit: str) -> int:
        return self._reps[self._normalize(digit)]

    @staticmethod
    def _normalize(digit: str) -> str:
        return "".join(sorted(digit))


def calculate_output_values(input_values: List[str]) -> List[int]:
    return [deduce_output_value(value) for value in input_values]


def deduce_output_value(input_signal: str) -> int:
    input_part, output_part = input_signal.split("|")

    input_digits = input_part.split()
    output_digits = output_part.split()

    occurences = Counter("".join(input_digits)).most_common(7)

    # When summing all 10 values - each segment has a constant number of showings.
    # RL - 9
    # LU - 6
    # LL - 4
    # RU and U - 8
    # L and M - 7
    right_lower = next(char for char, count in occurences if count == 9)
    left_upper = next(char for char, count in occurences if count == 6)
    left_lower = next(char for char, count in occurences if count == 4)

    # Use unique number to check against.
    one_rep = next(digit for digit in input_digits if len(digit) == 2)
    right_upper = one_rep.replace(right_lower, "")

    # Use other value with shared showing count.
    upper = next(char for char, count in occurences if count == 8 and char != right_upper)

    # Use unique number to check against.
    four_rep = next(digit for digit in input_digits if len(digit) == 4)
    middle = four_rep.replace(left_upper, "").replace(right_upper, "").replace(right_lower, "")

    # Use other value with shared showing count.
    lower = next(char for char, count in occurences if count == 7 and char != middle)

    clock = DigitClock(u=upper, lu=left_upper, ru=right_upper, m=middle, ll=left_lower, rl=right_lower, l=lower)

    str_nums = [str(clock.interpret(digit)) for digit in output_digits]

    return int("".join(str_nums))


if __name__ == "__main__":
    print(sum(calculate_output_values(get_input())))
