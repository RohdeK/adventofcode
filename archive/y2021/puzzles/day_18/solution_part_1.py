from typing import Iterator, List, Optional, Tuple, Union

from archive.y2021.puzzles.day_18.input_part_1 import get_input, SnailNumberListRep


class SnailNumber:
    def __init__(self, first: Union[int, "SnailNumber"], second: Union[int, "SnailNumber"]):
        self.first = first
        self.second = second

        self.parent: Optional["SnailNumber"] = None

        if not self.first_is_int():
            self.first.parent = self

        if not self.second_is_int():
            self.second.parent = self

    def first_is_int(self) -> bool:
        return isinstance(self.first, int)

    def second_is_int(self) -> bool:
        return isinstance(self.second, int)

    def magnitude(self) -> int:
        if isinstance(self.first, int):
            first_part_magnitude = self.first
        else:
            first_part_magnitude = self.first.magnitude()

        if isinstance(self.second, int):
            second_part_magnitude = self.second
        else:
            second_part_magnitude = self.second.magnitude()

        return 3 * first_part_magnitude + 2 * second_part_magnitude

    def __add__(self, other: "SnailNumber") -> "SnailNumber":
        sum_number = SnailNumber(first=self, second=other)

        sum_number.breakdown()

        return sum_number

    def remove(self, child: "SnailNumber") -> None:
        if self.first is child:
            self.first = 0
        elif self.second is child:
            self.second = 0
        else:
            raise ValueError(f"Not a parent of {child}")

    def walk_numerals(self, depth=0) -> Iterator[Tuple["SnailNumber", int]]:
        if isinstance(self.first, int):
            yield self, depth
        else:
            yield from self.first.walk_numerals(depth + 1)

        if isinstance(self.second, int):
            if not isinstance(self.first, int):
                yield self, depth
        else:
            yield from self.second.walk_numerals(depth + 1)

    def breakdown(self) -> None:
        while True:
            work_done = self.breakdown_explode()

            if work_done:
                continue

            work_done = self.breakdown_split()

            if work_done:
                continue

            break

    def breakdown_split(self) -> bool:
        found_split_value = False

        for sub_number, _ in self.walk_numerals():
            if isinstance(sub_number.first, int) and sub_number.first >= 10:
                new_number = self.pair_split(sub_number.first)
                sub_number.first = new_number
                new_number.parent = sub_number

                found_split_value = True
                break
            elif isinstance(sub_number.second, int) and sub_number.second >= 10:
                new_number = self.pair_split(sub_number.second)
                sub_number.second = new_number
                new_number.parent = sub_number

                found_split_value = True
                break

        return found_split_value

    @staticmethod
    def pair_split(value: int) -> "SnailNumber":
        half = value // 2
        return SnailNumber(first=half, second=value - half)

    def breakdown_explode(self) -> bool:
        found_explode_value = False

        for iter_number, depth in self.walk_numerals():
            if depth == 4:
                iter_number.explode()

                found_explode_value = True
                break

        return found_explode_value

    def explode(self) -> None:
        prev_numeral, on_left = self.previous_numeral()
        if prev_numeral:
            if on_left:
                prev_numeral.first += self.first
            else:
                prev_numeral.second += self.first

        next_numeral, on_right = self.next_numeral()
        if next_numeral:
            if on_right:
                next_numeral.second += self.second
            else:
                next_numeral.first += self.second

        self.parent.remove(self)

    def previous_numeral(self) -> Tuple[Optional["SnailNumber"], bool]:
        if not self.parent:
            return None, False

        iter_node = self

        while True:
            # Going up until I can move left
            if not iter_node.parent:
                return None, False

            # Up the chain until this iteration node is the second one
            if iter_node is iter_node.parent.second:
                iter_node = iter_node.parent
                break

            iter_node = iter_node.parent

        # If left is already a number
        if iter_node.first_is_int():
            return iter_node, True

        # Going left one step
        iter_node = iter_node.first

        while True:
            # Going down the chain to the right until a node with int right is met.
            if iter_node.second_is_int():
                return iter_node, False

            iter_node = iter_node.second

    def next_numeral(self) -> Tuple[Optional["SnailNumber"], bool]:
        if not self.parent:
            return None, False

        iter_node = self

        while True:
            # Going up until I can move right
            if not iter_node.parent:
                return None, False

            # Up the chain until this iteration node is the first one
            if iter_node is iter_node.parent.first:
                iter_node = iter_node.parent
                break

            iter_node = iter_node.parent

        # If right is already a number
        if iter_node.second_is_int():
            return iter_node, True

        # Going right one step
        iter_node = iter_node.second

        while True:
            # Going down the chain to the left until a node with int left is met.
            if iter_node.first_is_int():
                return iter_node, False

            iter_node = iter_node.first

    def add_value_to_rightmost(self, add: int) -> None:
        immediate_prev = None

        for immediate_prev, _ in self.walk_numerals():
            pass

        assert immediate_prev and isinstance(immediate_prev.second, int)

        immediate_prev.second += add

    def add_value_to_leftmost(self, add: int) -> None:
        for immediate_next, _ in self.walk_numerals():

            assert isinstance(immediate_next.first, int)

            immediate_next.first += add
            break

    @classmethod
    def from_rep(cls, rep: SnailNumberListRep) -> "SnailNumber":
        part_1_parsed = rep[0] if isinstance(rep[0], int) else SnailNumber.from_rep(rep[0])
        part_2_parsed = rep[1] if isinstance(rep[1], int) else SnailNumber.from_rep(rep[1])

        parsed = SnailNumber(first=part_1_parsed, second=part_2_parsed)

        return parsed

    def to_rep(self) -> SnailNumberListRep:
        first_rep = self.first if self.first_is_int() else self.first.to_rep()
        second_rep = self.second if self.second_is_int() else self.second.to_rep()

        return [first_rep, second_rep]

    def __repr__(self) -> str:
        return str(self.to_rep())


def calculate_solution(input_values: List[SnailNumberListRep]) -> int:
    snail_numbers = [SnailNumber.from_rep(rep) for rep in input_values]

    final_number = snail_numbers.pop(0)

    while snail_numbers:
        final_number += snail_numbers.pop(0)

    return final_number.magnitude()


if __name__ == "__main__":
    print(calculate_solution(get_input()))
