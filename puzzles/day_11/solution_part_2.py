
from puzzles.day_11.load_inputs import input_reader, InputType
from puzzles.day_11.solution_part_1 import Jungle, Monkey, parse_monkey


class UnhingedMonkey(Monkey):
    BOREDNESS_WORRY_DECAY = 1

    def lose_interest(self, item_level: str) -> int:
        return item_level % self.BOREDNESS_WORRY_DECAY


def calculate_solution(input_values: InputType) -> int:

    jungle = Jungle()

    for monkey_desc in input_values:
        monkey = parse_monkey(monkey_desc, UnhingedMonkey)
        jungle.add_monkey(monkey)

    test_divisible = 1
    for mk in jungle.monkeys.values():
        test_divisible *= mk.test_divisible

    UnhingedMonkey.BOREDNESS_WORRY_DECAY = test_divisible

    jungle.run_rounds(10000)

    most_active_monkeys = jungle.most_active(2)

    return most_active_monkeys[0].inspects * most_active_monkeys[1].inspects


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
