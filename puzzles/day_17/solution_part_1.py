import math
from collections import defaultdict
from typing import Dict, Tuple

from puzzles.day_17.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import PlanarMap, Position


class LavaMap(PlanarMap):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.distances: Dict[Position, float] = defaultdict(lambda: math.inf)

    def measure_entire_distance(self) -> int:
        self.distances.clear()
        self.distances[(1, 1)] = 0

        i = 1

        while i <= self.max_col:
            j = 1

            while j <= self.max_row:
                back_optimization = self.measure_from_node((i, j))

                if back_optimization:
                    # Return back some steps to do re-evaluation.
                    i = max(1, i - 2)
                    break

                j += 1

            i += 1

        return int(self.distances[(self.max_row, self.max_col)])

    def measure_from_node(self, node: Position) -> bool:
        this_node_distance = self.distances[node]
        assert this_node_distance is not math.inf

        self.measure_neighbor_node(this_node_distance, (node[0] + 1, node[1]))
        self.measure_neighbor_node(this_node_distance, (node[0], node[1] + 1))

        # Check back direction if a path updated.
        back_opt_1 = self.measure_neighbor_node(this_node_distance, (node[0] - 1, node[1]))
        back_opt_2 = self.measure_neighbor_node(this_node_distance, (node[0], node[1] - 1))

        return back_opt_1 or back_opt_2

    def measure_neighbor_node(self, distance: float, neighbor: Position) -> bool:
        try:
            value_of_neighbor = int(self.tiles_by_loc[neighbor].type)
        except KeyError:
            pass
        else:
            distance_of_neighbor = distance + value_of_neighbor

            if distance_of_neighbor < self.distances[neighbor]:
                self.distances[neighbor] = distance_of_neighbor

                return True

        return False


def calculate_solution(input_values: InputType) -> int:
    lava_map = LavaMap(input_values[0])

    return lava_map.measure_entire_distance()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
