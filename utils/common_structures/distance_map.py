import math
from collections import defaultdict

from utils.common_structures.planar_map import Location, PlanarMap, Position


class DistanceMap(PlanarMap):
    def __init__(self, locations: list[Location]):
        super().__init__(locations)
        self._node_distances: dict[Position, float] = defaultdict(lambda: math.inf)
        self._distance_types: dict[str, float] = defaultdict(lambda: 1)
        self.start_position = None
        self.end_position = None
        self._cheapest_routes = {}

    def set_starting_position(self, pos: Position) -> None:
        self.start_position = pos
        self._node_distances[self.start_position] = 0

    def set_starting_type(self, ttype: str) -> None:
        assert len(self.tiles_by_type[ttype]) == 1
        self.set_starting_position(self.tiles_by_type[ttype][0].position())

    def set_end_position(self, pos: Position) -> None:
        self.end_position = pos

    def set_ending_type(self, ttype: str) -> None:
        assert len(self.tiles_by_type[ttype]) == 1
        self.end_position = self.tiles_by_type[ttype][0].position()

    def distance_weight_of(self, loc: Location):
        return self._distance_types[loc.type]

    def update_type_weight(self, ttype: str, weight: float) -> None:
        self._distance_types[ttype] = weight

    def measure_neighbor(self, loc: Location, neighbor: Location) -> bool:
        if neighbor is None:
            return False

        node_distance = self._node_distances[loc.position()]

        neighbor_dist = self.distance_weight_of(neighbor)

        if node_distance + neighbor_dist < self._node_distances[neighbor.position()]:
            self._node_distances[neighbor.position()] = node_distance + neighbor_dist
            self._cheapest_routes[neighbor.position()] = loc.position()
            return True

        return False

    def measure_distances(self) -> int:
        positions_to_check: list[Position] = [self.start_position]

        while positions_to_check:
            row, col = positions_to_check.pop(0)
            node = self.get_location(row, col)

            this_node_distance = self._node_distances[(row, col)]
            assert this_node_distance is not math.inf

            for neighbor in self.surrounding(node, including_diagonals=False):
                if self.measure_neighbor(node, neighbor):
                    positions_to_check.append(neighbor.position())

        return int(self._node_distances[self.end_position])

    def print_fastest_route(self) -> None:
        printsplice = self.splice()
        pos = self.end_position

        while pos != self.start_position:
            tile = printsplice.tiles_by_loc[pos]
            if tile.type == ".":
                printsplice.change_type(tile, "O")
            else:
                printsplice.change_type(tile, "X")
            pos = self._cheapest_routes[tile.position()]

        print("\n")
        print(printsplice)

    def nodes_and_distances(self) -> dict[Position, float]:
        return dict(self._node_distances)
