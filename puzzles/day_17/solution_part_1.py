import math
from collections import defaultdict
from typing import Dict

from puzzles.day_17.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import PlanarMap, Position


class LavaMap(PlanarMap):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.distances: Dict[Position, float] = defaultdict(lambda: math.inf)
        self.shortest_paths_from: Dict[Position, Position] = {}
        self.shortest_paths_dirs: Dict[Position, str] = {}
        self.curr_node = None

    def measure_entire_distance(self) -> int:
        self.distances.clear()
        self.shortest_paths_from.clear()
        self.distances[(1, 1)] = 0
        self.shortest_paths_dirs[(1, 1)] = ""

        i = 1

        while i <= self.max_col:
            j = 1

            while j <= self.max_row:
                back_optimization = self.measure_from_node((i, j))

                if back_optimization:
                    # Return back some steps to do re-evaluation.
                    i = max(1, i - 3)
                    break

                j += 1

            i += 1

        return int(self.distances[(self.max_row, self.max_col)])

    def measure_from_node(self, node: Position) -> bool:
        self.curr_node = node
        this_node_distance = self.distances[node]
        if this_node_distance is math.inf:
            return False
        # assert this_node_distance is not math.inf, node

        to_bottom = (node[0] + 1, node[1])
        to_right = (node[0], node[1] + 1)
        to_top = (node[0] - 1, node[1])
        to_left = (node[0], node[1] - 1)
        node_dir_path = self.shortest_paths_dirs[node]

        if not node_dir_path.endswith("vvv"):
            bottom_opt = self.measure_neighbor_node(this_node_distance, to_bottom)
            if bottom_opt:
                self.shortest_paths_dirs[to_bottom] = node_dir_path + "v"

        if not node_dir_path.endswith(">>>"):
            right_opt = self.measure_neighbor_node(this_node_distance, to_right)
            if right_opt:
                self.shortest_paths_dirs[to_right] = node_dir_path + ">"

        # Check back direction if a path updated.
        top_opt = False
        if not node_dir_path.endswith("^^^"):
            top_opt = self.measure_neighbor_node(this_node_distance, to_top)
            if top_opt:
                self.shortest_paths_dirs[to_top] = node_dir_path + "^"

        left_opt = False
        if not node_dir_path.endswith("<<<"):
            left_opt = self.measure_neighbor_node(this_node_distance, to_left)
            if left_opt:
                self.shortest_paths_dirs[to_left] = node_dir_path + "<"

        return left_opt or top_opt

    def measure_neighbor_node(self, distance: float, neighbor: Position) -> bool:
        try:
            value_of_neighbor = int(self.tiles_by_loc[neighbor].type)
        except KeyError:
            pass
        else:
            distance_of_neighbor = distance + value_of_neighbor

            if distance_of_neighbor < self.distances[neighbor]:
                self.distances[neighbor] = distance_of_neighbor
                self.shortest_paths_from[neighbor] = self.curr_node

                return True

        return False


def calculate_solution(input_values: InputType) -> int:
    print("\n")
    lava_map = LavaMap(input_values[0])

    distance = lava_map.measure_entire_distance()

    iter_step = (lava_map.max_row, lava_map.max_col)
    print(lava_map.shortest_paths_dirs[iter_step])
    while iter_step:
        lava_map.tiles_by_loc[iter_step].type = "#"
        iter_step = lava_map.shortest_paths_from.get(iter_step)

    print(lava_map)
    return distance


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
