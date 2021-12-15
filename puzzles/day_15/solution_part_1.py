import math
from collections import defaultdict
from typing import Dict, List, Tuple

from puzzles.day_15.input_part_1 import get_input


class WeightedGraph:
    def __init__(self, input_values: List[List[int]]):
        self._node_values: Dict[Tuple[int, int], int] = {
            (col_index, row_index): value
            for row_index, row in enumerate(input_values)
            for col_index, value in enumerate(row)
        }
        self._width = len(input_values[0])
        self._height = len(input_values)
        self._node_distances: Dict[Tuple[int, int], float] = defaultdict(lambda: math.inf)
        self._node_distances[(0, 0)] = 0

    def measure_entire_distance(self) -> int:
        for i in range(self._width):
            for j in range(self._height):
                self.measure_from_node((i, j))

        return int(self._node_distances[(self._width - 1, self._height - 1)])

    def measure_from_node(self, node: Tuple[int, int]) -> None:
        this_node_distance = self._node_distances[node]
        assert this_node_distance is not math.inf

        self.measure_neighbor_node(this_node_distance, (node[0] + 1, node[1]))
        self.measure_neighbor_node(this_node_distance, (node[0], node[1] + 1))

    def measure_neighbor_node(self, node_distance: float, neighbor: Tuple[int, int]) -> None:
        try:
            value_of_neighbor = self._node_values[neighbor]
        except KeyError:
            pass
        else:
            distance_of_neighbor = node_distance + value_of_neighbor

            if distance_of_neighbor < self._node_distances[neighbor]:
                self._node_distances[neighbor] = distance_of_neighbor


def shortest_path_length(input_values: List[List[int]]) -> int:
    return WeightedGraph(input_values).measure_entire_distance()


if __name__ == "__main__":
    print(shortest_path_length(get_input()))
