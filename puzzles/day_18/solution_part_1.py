from collections import defaultdict
from itertools import permutations
from typing import Dict, List

from puzzles.day_18.load_inputs import Cubelet, input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    per_vertex: List[Dict[int, InputType]] = [
        defaultdict(list),
        defaultdict(list),
        defaultdict(list),
    ]

    for cube in input_values:
        for i in range(3):
            per_vertex[i][cube[i]].append(cube)

    adjacencies = 0

    for overlap_facet in range(3):
        overlap_vertices = [v for v in range(3) if v != overlap_facet]

        first_vertex = overlap_vertices[0]
        second_vertex = overlap_vertices[1]

        for cube in input_values:
            first_overlaps = per_vertex[first_vertex][cube[first_vertex]]
            second_overlaps = per_vertex[second_vertex][cube[second_vertex]]

            overlaps = [c for c in first_overlaps if c in second_overlaps]
            adjacent = [c for c in overlaps if abs(c[overlap_facet] - cube[overlap_facet]) == 1]
            adjacencies += len(adjacent)

    return len(input_values) * 6 - adjacencies


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
