from typing import List, Tuple

from puzzles.day_19.load_inputs import (
    Condition,
    Decider,
    LargerCondition,
    Object,
    Rule,
    SmallerCondition,
    input_reader,
    InputType,
)


class MultiCondition(Condition):
    def __init__(self, *conds: Condition):
        self.sub_conditions = []
        for c in conds:
            if c is None:
                continue
            if isinstance(c, MultiCondition):
                self.sub_conditions.extend(c.sub_conditions)
            else:
                self.sub_conditions.append(c)

    def apply(self, o: Object) -> bool:
        return all(c.apply(o) for c in self.sub_conditions)

    def __repr__(self):
        return " and ".join(repr(c) for c in self.sub_conditions)


def reverse_rule_merge(rules: List[Rule]) -> Rule:
    while len(rules) > 1:
        finalizable_rules = [
            r for r in rules if all(d.then in ("A", "R") for d in r.deciders)
        ]

        for rule in finalizable_rules:
            rules.remove(rule)

            depending_rules = [
                r for r in rules if any(d.then == rule.name for d in r.deciders)
            ]

            for dep_rule in depending_rules:
                for idx, dec in enumerate(dep_rule.deciders):
                    if dec.then == rule.name:
                        dep_rule.deciders.remove(dec)

                        for sub_dec in rule.deciders[::-1]:
                            if dec.condition is None:
                                combined_condition = sub_dec.condition
                            else:
                                combined_condition = MultiCondition(
                                    dec.condition, sub_dec.condition
                                )

                            combined_decider = Decider(
                                then=sub_dec.then,
                                condition=combined_condition,
                            )
                            dep_rule.deciders.insert(idx, combined_decider)

                        break

    return rules[0]


BoxType = Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int]]


def calc_box_size(box: BoxType) -> int:
    return (
        (box[0][1] - box[0][0] + 1)
        * (box[1][1] - box[1][0] + 1)
        * (box[2][1] - box[2][0] + 1)
        * (box[3][1] - box[3][0] + 1)
    )


def remove_box(
    curr_boxes: List[BoxType], to_remove: BoxType
) -> Tuple[List[BoxType], List[BoxType]]:
    remaining_boxes = []
    removed_parts = []

    for box in curr_boxes:
        box_size = calc_box_size(box)

        x_overlap = (max(box[0][0], to_remove[0][0]), min(box[0][1], to_remove[0][1]))
        m_overlap = (max(box[1][0], to_remove[1][0]), min(box[1][1], to_remove[1][1]))
        a_overlap = (max(box[2][0], to_remove[2][0]), min(box[2][1], to_remove[2][1]))
        s_overlap = (max(box[3][0], to_remove[3][0]), min(box[3][1], to_remove[3][1]))

        if (
            x_overlap[0] > x_overlap[1]
            or m_overlap[0] > m_overlap[1]
            or a_overlap[0] > a_overlap[1]
            or s_overlap[0] > s_overlap[1]
        ):
            remaining_boxes.append(box)
            continue

        removed_size = calc_box_size((x_overlap, m_overlap, a_overlap, s_overlap))
        removed_parts.append((x_overlap, m_overlap, a_overlap, s_overlap))

        kept_size = 0

        x_keep = [
            (box[0][0], min(to_remove[0][0] - 1, box[0][1])),
            (max(to_remove[0][1] + 1, box[0][0]), box[0][1]),
        ]
        x_keep = [x for x in x_keep if x[0] <= x[1]]

        for x_box in x_keep:
            kept_size += calc_box_size((x_box, box[1], box[2], box[3]))
            remaining_boxes.append((x_box, box[1], box[2], box[3]))

        m_keep = [
            (box[1][0], min(to_remove[1][0] - 1, box[1][1])),
            (max(to_remove[1][1] + 1, box[1][0]), box[1][1]),
        ]
        m_keep = [m for m in m_keep if m[0] <= m[1]]

        for m_box in m_keep:
            kept_size += calc_box_size((x_overlap, m_box, box[2], box[3]))
            remaining_boxes.append((x_overlap, m_box, box[2], box[3]))

        a_keep = [
            (box[2][0], min(to_remove[2][0] - 1, box[2][1])),
            (max(to_remove[2][1] + 1, box[2][0]), box[2][1]),
        ]
        a_keep = [a for a in a_keep if a[0] <= a[1]]

        for a_box in a_keep:
            kept_size += calc_box_size((x_overlap, m_overlap, a_box, box[3]))
            remaining_boxes.append((x_overlap, m_overlap, a_box, box[3]))

        s_keep = [
            (box[3][0], min(to_remove[3][0] - 1, box[3][1])),
            (max(to_remove[3][1] + 1, box[3][0]), box[3][1]),
        ]
        s_keep = [s for s in s_keep if s[0] <= s[1]]

        for s_box in s_keep:
            kept_size += calc_box_size((x_overlap, m_overlap, a_overlap, s_box))
            remaining_boxes.append((x_overlap, m_overlap, a_overlap, s_box))

        assert kept_size + removed_size == box_size

    return remaining_boxes, removed_parts


def calculate_solution(input_values: InputType) -> int:
    rules, objects = input_values

    rule = reverse_rule_merge(rules)

    unsolved_boxes = [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]
    resolved_a_boxes = []
    resolved_r_boxes = []

    i = len(rule.deciders)
    for decider in rule.deciders:
        print(i, "remaining")

        full_box = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
        conds = (
            decider.condition.sub_conditions
            if isinstance(decider.condition, MultiCondition)
            else [decider.condition]
        )
        for condition in conds:
            if condition is None:
                continue
            if isinstance(condition, LargerCondition):
                full_box[condition.variable] = (
                    max(full_box[condition.variable][0], condition.threshold + 1),
                    full_box[condition.variable][1],
                )
            elif isinstance(condition, SmallerCondition):
                full_box[condition.variable] = (
                    full_box[condition.variable][0],
                    min(full_box[condition.variable][1], condition.threshold - 1),
                )
            else:
                raise TypeError(condition)

        new_unresolved, current_resolved = remove_box(
            unsolved_boxes, (full_box["x"], full_box["m"], full_box["a"], full_box["s"])
        )
        before_sum = sum(calc_box_size(r) for r in unsolved_boxes)
        after_sum = sum(calc_box_size(r) for r in new_unresolved)
        c_sum = sum(calc_box_size(r) for r in current_resolved)
        assert c_sum == before_sum - after_sum
        unsolved_boxes = new_unresolved

        if decider.then == "A":
            resolved_a_boxes.extend(current_resolved)
        if decider.then == "R":
            resolved_r_boxes.extend(current_resolved)

        a_sum = sum(calc_box_size(r) for r in resolved_a_boxes)
        r_sum = sum(calc_box_size(r) for r in resolved_r_boxes)
        assert after_sum + a_sum + r_sum == 256_000_000_000_000
        i -= 1

    # NOT 132381983097922
    return sum(calc_box_size(r) for r in resolved_a_boxes)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
