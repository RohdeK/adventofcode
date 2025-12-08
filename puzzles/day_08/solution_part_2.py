from functools import reduce

from puzzles.day_08.load_inputs import input_reader, InputType
from puzzles.day_08.solution_part_1 import gather_distances


def calculate_solution(input_values: InputType) -> int:
    distances = gather_distances(input_values)

    all_circuits: list[set] = []

    for (x1, x2), _ in distances:
        circuits_to_join = []

        for circ in all_circuits:
            if x1 in circ or x2 in circ:
                circ.add(x1)
                circ.add(x2)
                circuits_to_join.append(circ)

        if len(circuits_to_join) > 1:
            new_circ = reduce(set.union, circuits_to_join)

            for circ in circuits_to_join:
                all_circuits.remove(circ)

            all_circuits.append(new_circ)

        elif len(circuits_to_join) == 1:
            pass

        elif len(circuits_to_join) == 0:
            all_circuits.append({x1, x2})

        if len(all_circuits) == 1 and len(all_circuits[0]) == len(input_values):
            print("break at", x1, x2)

            return x1[0] * x2[0]


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
