import itertools
import math
from functools import reduce

from puzzles.day_08.load_inputs import input_reader, InputType


def distance(x1: list[int], x2: list[int]) -> float:
    return math.sqrt(sum((x1i - x2i)**2 for x1i, x2i in zip(x1, x2)))


def gather_distances(
    input_values: InputType
) -> list[tuple[tuple[tuple[int, ...], tuple[int, ...]], float]]:
    distances = {}

    for x1, x2 in itertools.combinations(input_values, 2):
        distances[(tuple(x1), tuple(x2))] = distance(x1, x2)

    return sorted(distances.items(), key=lambda x: x[1])


def calculate_solution(input_values: InputType, connections: int) -> int:
    top_conns = gather_distances(input_values)[:connections]

    all_circuits = [{x1, x2} for (x1, x2), _ in top_conns]

    all_len = len(reduce(set.union, all_circuits))

    while sum(len(c) for c in all_circuits) > all_len:
        for circ1, circ2 in itertools.combinations(all_circuits, 2):
            if circ1.intersection(circ2):
                all_circuits.remove(circ1)
                all_circuits.remove(circ2)
                all_circuits.append(circ1.union(circ2))
                break

    top_3 = sorted(all_circuits, key=len, reverse=True)[:3]

    return reduce(lambda x, y: x * y, map(len, top_3))


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input, 1000))
