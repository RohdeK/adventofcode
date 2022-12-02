from collections import defaultdict
from typing import List

from archive.y2021.puzzles.day_24.input_part_1 import get_input


class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            ret = self[key] = self.default_factory(key)
            return ret


def perform_calculations(start_number: int, steps: List[str]) -> bool:
    numbers = [int(i) for i in list(str(start_number))]
    index = 0

    def next_input() -> int:
        nonlocal index
        next_num = numbers[index]
        index += 1
        return next_num

    by_literal = keydefaultdict(lambda lit: int(lit))
    by_literal.update(
        {
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0,
        }
    )

    for step in steps:
        if step.startswith("inp"):
            val = step.replace("inp ", "")
            by_literal[val] = next_input()

        elif step.startswith("add"):
            val1, val2 = step.replace("add ", "").split(" ")
            by_literal[val1] += by_literal[val2]

        elif step.startswith("mul"):
            val1, val2 = step.replace("mul ", "").split(" ")
            by_literal[val1] *= by_literal[val2]

        elif step.startswith("mod"):
            val1, val2 = step.replace("mod ", "").split(" ")
            by_literal[val1] %= by_literal[val2]

        elif step.startswith("div"):
            val1, val2 = step.replace("div ", "").split(" ")
            by_literal[val1] //= by_literal[val2]

        elif step.startswith("eql"):
            val1, val2 = step.replace("eql ", "").split(" ")
            by_literal[val1] = int(by_literal[val1] == by_literal[val2])

        else:
            raise ValueError(step)

    return by_literal["z"] == 0


def calculate_solution(input_values: List[str]) -> int:
    # i = 92915979999498
    i = 21611513911181
    """
    [[I6 == I5 + 4]]
    [[I8 == I7 + 2]]
    [[I9 == I4 + 8]]
    [[I11 == I10]]
    [[I12 == I3 - 5]]
    [[I13 == I2 + 7]]
    [[I14 == I1 - 1]]
    
    I1 = 9 => I14 = 8
    I2 = 2 => I13 = 9
    I3 = 9 => I12 = 4
    I4 = 1 => I9 = 9
    I5 = 5 => I6 = 9
    I7 = 7 => I8 = 9
    I10 = 9 => I11 = 9
    
    92915979999498
    
    
    I1 = 2 => I14 = 1
    I2 = 1 => I13 = 8
    I3 = 6 => I12 = 1
    I4 = 1 => I9 = 9
    I5 = 1 => I6 = 5
    I7 = 1 => I8 = 3
    I10 = 1 => I11 = 1
    
    21611513911181
    """

    while True:
        if perform_calculations(i, input_values):
            return i
        i = i - 1


if __name__ == "__main__":
    print(calculate_solution(get_input()))
