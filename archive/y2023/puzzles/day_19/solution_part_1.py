from archive.y2023.puzzles.day_19.load_inputs import input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    rules, objects = input_values
    rule_map = {rule.name: rule for rule in rules}

    accepted = []

    for obj in objects:
        target = "in"

        while target not in ("A", "R"):
            rule = rule_map[target]
            target = rule.apply(obj)

        if target == "A":
            accepted.append(obj)

    return sum(v for o in accepted for v in (o.x, o.m, o.a, o.s))


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
