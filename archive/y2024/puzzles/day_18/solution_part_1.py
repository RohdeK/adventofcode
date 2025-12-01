import math
from collections import defaultdict

from puzzles.day_18.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Location, PlanarMap, Position


class MemoryMap(PlanarMap):
    def __init__(self, locations: list[Location]):
        super().__init__(locations)
        self._node_distances: dict[Position, float] = defaultdict(lambda: math.inf)
        self.start_position = (0, 0)
        self.end_position = (self.max_col, self.max_row)
        self._node_distances[self.start_position] = 0
        self._cheapest_routes = {}

    def measure_from(self, loc: Location) -> bool:
        this_node_distance = self._node_distances[loc.position()]
        assert this_node_distance is not math.inf

        self.measure_neighbor(loc, self.get_location_south(loc))
        self.measure_neighbor(loc, self.get_location_east(loc))

        # Check back direction if a path updated.
        back_opt_1 = self.measure_neighbor(loc, self.get_location_north(loc))
        back_opt_2 = self.measure_neighbor(loc, self.get_location_west(loc))

        return back_opt_1 or back_opt_2

    def measure_neighbor(self, loc: Location, neighbor: Location) -> bool:
        if neighbor is None:
            return False

        node_distance = self._node_distances[loc.position()]

        neighbor_dist = 1 if neighbor.type == "." else 1000000000

        if node_distance + neighbor_dist < self._node_distances[neighbor.position()]:
            self._node_distances[neighbor.position()] = node_distance + neighbor_dist
            self._cheapest_routes[neighbor.position()] = loc.position()
            return True

        return False

    def measure_entire_distance_vertical(self) -> int:
        row = 0

        while row <= self.max_row:
            col = 0

            while col <= self.max_col:
                node = self.get_location(row, col)
                back_optimization = self.measure_from(node)

                if back_optimization:
                    # Return back some steps to do re-evaluation.
                    row = max(0, row - 2)
                    break

                col += 1

            row += 1

        return int(self._node_distances[self.end_position])

    def measure_entire_distance_horizontal(self) -> int:
        col = 0

        while col <= self.max_col:
            row = 0

            while row <= self.max_row:
                node = self.get_location(row, col)
                back_optimization = self.measure_from(node)

                if back_optimization:
                    # Return back some steps to do re-evaluation.
                    col = max(0, col - 2)
                    break

                row += 1

            col += 1

        return int(self._node_distances[self.end_position])

    def measure_entire_distance(self) -> int:
        horizontal = self.splice()
        h_value = horizontal.measure_entire_distance_horizontal()

        vertical = self.splice()
        v_value = vertical.measure_entire_distance_vertical()

        if v_value < h_value:
            return self.measure_entire_distance_vertical()
        else:
            return self.measure_entire_distance_horizontal()

    def print_fastest_route(self) -> None:
        pos = self.end_position

        while pos != self.start_position:
            tile = self.tiles_by_loc[pos]
            if tile.type == ".":
                self.change_type(tile, "O")
            else:
                print(tile.position)
            pos = self._cheapest_routes[tile.position()]

        print("\n")
        print(self)


def calculate_solution(input_values: InputType, numlocs: int, gridsize: Position) -> int:
    input_values = [tuple(val) for val in input_values[:numlocs]]
    locations = []
    for col in range(gridsize[0] + 1):
        for row in range(gridsize[1] + 1):
            if (col, row) in input_values:
                locations.append(Location(row, col, "#"))
            else:
                locations.append(Location(row, col, "."))

    memmap = MemoryMap(locations)

    val = memmap.measure_entire_distance()

    # memmap.print_fastest_route()

    return val


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input, 1024, (70, 70)))
