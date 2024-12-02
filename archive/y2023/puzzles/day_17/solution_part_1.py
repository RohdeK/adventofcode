import math
from collections import defaultdict
from typing import Dict, List, Set

from puzzles.day_17.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Location, PlanarMap, Position


class LavaMap(PlanarMap):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.distances: Dict[Position, float] = defaultdict(lambda: math.inf)
        self.shortest_paths_from: Dict[Position, Position] = {}
        self.shortest_paths_dirs: Dict[Position, str] = {}
        self.curr_node = None
        self.interesting_corners: Set[Position] = set()

    def measure_entire_distance(self, omit_corners: List[Position] = None) -> int:
        self.distances.clear()
        self.shortest_paths_from.clear()
        self.shortest_paths_dirs.clear()
        self.curr_node = None
        self.distances[(1, 1)] = 0
        self.shortest_paths_dirs[(1, 1)] = ""
        self.interesting_corners.clear()
        omit_corners = omit_corners or []

        self.horizontally_scan(omit_corners)
        self.vertically_scan(omit_corners)

        return int(self.distances[(self.max_row, self.max_col)])

    def horizontally_scan(self, omit_corners: List[Position]) -> None:
        i = 1
        delayed_back_optimization = False
        fulfilled_delayed_back_optimization = True

        while i <= self.max_col:
            j = 1
            if fulfilled_delayed_back_optimization is False:
                i = max(1, i - 2)
                fulfilled_delayed_back_optimization = True

            if delayed_back_optimization:
                fulfilled_delayed_back_optimization = False
                delayed_back_optimization = False
            else:
                fulfilled_delayed_back_optimization = True

            while j <= self.max_row:
                if self.distances[(i, j)] is math.inf:
                    if i > 2:
                        delayed_back_optimization = True
                else:
                    if (i, j) in omit_corners:
                        back_optimization = False
                    else:
                        back_optimization = self.measure_from_node((i, j))

                    if back_optimization:
                        # Return back some steps to do re-evaluation.
                        i = max(1, i - 2)
                        break

                j += 1

            i += 1

    def vertically_scan(self, omit_corners: List[Position]) -> None:
        j = 1
        delayed_back_optimization = False
        fulfilled_delayed_back_optimization = True

        while j <= self.max_row:
            i = 1
            if fulfilled_delayed_back_optimization is False:
                j = max(1, j - 2)
                fulfilled_delayed_back_optimization = True

            if delayed_back_optimization:
                fulfilled_delayed_back_optimization = False
                delayed_back_optimization = False
            else:
                fulfilled_delayed_back_optimization = True

            while i <= self.max_col:
                if self.distances[(j, i)] is math.inf:
                    if j > 2:
                        delayed_back_optimization = True
                else:
                    if (j, i) in omit_corners:
                        back_optimization = False
                    else:
                        back_optimization = self.measure_from_node((j, i))

                    if back_optimization:
                        # Return back some steps to do re-evaluation.
                        j = max(1, j - 2)
                        break

                i += 1

            j += 1

    def get_shortest_path(self) -> List[Position]:
        final_step = (self.max_row, self.max_col)
        path = self.shortest_paths_dirs[final_step]

        position = (0, 0)
        positions = [position]
        for direction in path:
            if direction == ">":
                position = position[0], position[1] + 1
            elif direction == "<":
                position = position[0], position[1] - 1
            elif direction == "v":
                position = position[0] + 1, position[1]
            elif direction == "^":
                position = position[0], position[1] + 1
            positions.append(position)

        return positions

    def get_interesting_corners(self) -> Set[Position]:
        final_step = (self.max_row, self.max_col)
        positions = self.get_shortest_path()
        path = self.shortest_paths_dirs[final_step]

        to_check = set()
        curr_symb = None
        curr_seq = 0
        seq_start = None
        for idx, i in enumerate(path):
            if curr_symb == i:
                curr_seq += 1
            else:
                curr_symb = i
                seq_start = idx
                curr_seq = 1

            if curr_seq >= 2 and seq_start != 0:
                to_check.add(seq_start)

        return {positions[i] for i in to_check}

    def measure_from_node(self, node: Position) -> bool:
        self.curr_node = node
        # if node in [(1, 5), (4, 12), (6, 13)]:
        #     return False

        this_node_distance = self.distances[node]
        assert this_node_distance is not math.inf, node

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
            elif distance_of_neighbor == self.distances[neighbor]:
                curr_path = self.shortest_paths_dirs[neighbor]
                symb = {
                    (1, 0): "v",
                    (-1, 0): "^",
                    (0, 1): ">",
                    (0, -1): "<",
                }[(neighbor[0] - self.curr_node[0], neighbor[1] - self.curr_node[1])]
                expe_path = self.shortest_paths_dirs[self.curr_node] + symb

                if expe_path != curr_path and expe_path[-2:] == curr_path[-2:][::-1]:
                    self.interesting_corners.add(self.shortest_paths_from[neighbor])

        return False

    def print_path(self) -> None:
        iter_step = (self.max_row, self.max_col)
        keep_steps = []
        while iter_step:
            keep_steps.append(iter_step)
            # lava_map.tiles_by_loc[iter_step].type = "#"
            iter_step = self.shortest_paths_from.get(iter_step)

        new_tiles = [Location(row=t.row, col=t.col, type=t.type) for t in self.tiles]

        for tile in new_tiles:
            if tile.position() not in keep_steps:
                tile.type = "."

        print(PlanarMap(new_tiles))


def calculate_solution(input_values: InputType) -> int:
    print("\n")
    lava_map = LavaMap(input_values[0])

    distance = lava_map.measure_entire_distance()

    found_shorter = True
    corners_to_omit = []

    while found_shorter:
        found_shorter = False
        corners = lava_map.get_interesting_corners()
        corners = corners.union(lava_map.interesting_corners)
        for corner in corners:
            new_distance = lava_map.measure_entire_distance(corners_to_omit + [corner])
            if new_distance < distance:
                distance = new_distance
                corners_to_omit.append(corner)
                found_shorter = True
                break

    return distance


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
