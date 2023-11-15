import re
from typing import Callable, Dict, List

from archive.y2022.puzzles.day_11.load_inputs import input_reader, InputType


class Monkey:
    def __init__(self, index: int, operation: str, test_divisible: int, true_target: int, false_target: int):
        self.index = index
        self.inspects = 0
        self.operation = self.parse_operation(operation)
        self.items: List[int] = []
        self.on_throw: Callable[[int, int], None] = None
        self.test_divisible = test_divisible
        self.true_target = true_target
        self.false_target = false_target

    def __repr__(self):
        return f"{self.index}: {self.items}"

    def catch(self, item_level: int) -> None:
        self.items.append(item_level)

    def throw_all(self) -> None:
        while self.items:
            self.throw_next()

    def throw_next(self) -> None:
        next_item = self.items.pop(0)
        next_item = self.inspect(next_item)
        next_item = self.lose_interest(next_item)
        to_monkey = self.choose_throw_target(next_item)
        self.on_throw and self.on_throw(to_monkey, next_item)

    def inspect(self, item_level: int) -> int:
        self.inspects += 1
        return self.operation(item_level)

    def lose_interest(self, item_level: str) -> int:
        return item_level // 3

    def choose_throw_target(self, item_level: str) -> int:
        if item_level % self.test_divisible == 0:
            return self.true_target
        else:
            return self.false_target

    @staticmethod
    def parse_operation(op_desc: str) -> Callable[[int], int]:
        op_desc = op_desc.replace("new = ", "")
        return lambda old: eval(op_desc)


class Jungle:
    def __init__(self):
        self.monkeys: Dict[int, Monkey] = {}
        self.round_nr = 0

    def __repr__(self):
        monkeys_reps = "\n".join([repr(monkey) for monkey in self.monkeys.values()])
        return f"{self.round_nr}:\n{monkeys_reps}"

    def add_monkey(self, monkey: Monkey) -> None:
        self.monkeys[monkey.index] = monkey
        monkey.on_throw = self.direct_throw

    def direct_throw(self, at_monkey: int, item_level: int) -> None:
        self.monkeys[at_monkey].catch(item_level)

    def run_rounds(self, num_rounds: int) -> None:
        for _ in range(num_rounds):
            self.round_nr += 1
            self.run_round()

    def run_round(self) -> None:
        for index in sorted(self.monkeys.keys()):
            self.monkeys[index].throw_all()

    def most_active(self, num_active: int) -> List[Monkey]:
        return sorted(self.monkeys.values(), key=lambda x: x.inspects, reverse=True)[:num_active]


def parse_monkey(monkey_desc: List[str], mk_class=Monkey) -> Monkey:
    monkey_index = int(re.match(r"Monkey (\d+):", monkey_desc[0])[1])

    monkey_starting_items = monkey_desc[1].split("Starting items: ")[-1]
    monkey_starting_items = [int(item) for item in monkey_starting_items.split(", ")]

    monkey_operation = monkey_desc[2].split("Operation: ")[-1]

    monkey_divisible = int(monkey_desc[3].split("Test: divisible by ")[-1])

    monkey_true_target = int(monkey_desc[4].split("If true: throw to monkey ")[-1])
    monkey_false_target = int(monkey_desc[5].split("If false: throw to monkey ")[-1])

    monkey = mk_class(
        index=monkey_index,
        operation=monkey_operation,
        test_divisible=monkey_divisible,
        true_target=monkey_true_target,
        false_target=monkey_false_target,
    )

    for item in monkey_starting_items:
        monkey.catch(item)

    return monkey


def calculate_solution(input_values: InputType) -> int:
    jungle = Jungle()

    for monkey_desc in input_values:
        monkey = parse_monkey(monkey_desc)
        jungle.add_monkey(monkey)

    jungle.run_rounds(20)

    most_active_monkeys = jungle.most_active(2)

    return most_active_monkeys[0].inspects * most_active_monkeys[1].inspects


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
