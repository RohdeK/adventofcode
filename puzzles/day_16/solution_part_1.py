from collections import defaultdict
from typing import Dict, List, Set, Tuple

from puzzles.day_16.load_inputs import input_reader, InputType
from utils.common_structures.planar_map import Location, PlanarMap, Position


class MirrorMap(PlanarMap):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.equivalence_classes: Dict[int, List[Location]] = {}
        self.equivalence_entry_points: Dict[Position, List[Tuple[int, str]]] = defaultdict(list)
        self.equivalence_exit_points: Dict[int, List[Tuple[Location, str]]] = defaultdict(list)
        self.equivalence_classes_by_loc: Dict[Position, List[int]] = defaultdict(list)
        self._build_equivalence_classes()

    def _build_equivalence_classes(self) -> None:
        equiv_index = 0
        curr_equiv_class = []

        def finalize_equiv_class() -> int:
            nonlocal equiv_index
            nonlocal curr_equiv_class

            self.equivalence_classes[equiv_index] = curr_equiv_class
            for loc in curr_equiv_class:
                self.equivalence_classes_by_loc[loc.position()].append(equiv_index)

            curr_equiv_class = []
            equiv_index += 1

            return equiv_index - 1

        for row in self.tiles_by_row.values():
            curr_equiv_class = []
            tiles_to_cover = [tile for tile in row]

            while tiles_to_cover:
                tile = tiles_to_cover.pop(0)
                curr_equiv_class.append(tile)

                if tile.type in ("-", "|", "/", "\\"):
                    if tile.type == "|":
                        self.equivalence_exit_points[equiv_index].append((tile, "east"))
                        self.equivalence_exit_points[equiv_index].append((tile, "west"))
                    elif tile.type == "-":
                        self.equivalence_entry_points[tile.position()].append((equiv_index, "south"))
                        self.equivalence_entry_points[tile.position()].append((equiv_index, "north"))

                    if len(curr_equiv_class) == 1:
                        if tile.type == "/":
                            self.equivalence_entry_points[tile.position()].append((equiv_index, "south"))
                            self.equivalence_exit_points[equiv_index].append((tile, "east"))
                        elif tile.type == "\\":
                            self.equivalence_entry_points[tile.position()].append((equiv_index, "north"))
                            self.equivalence_exit_points[equiv_index].append((tile, "east"))
                    elif tile.type != "-":
                        if tile.type == "/":
                            self.equivalence_entry_points[tile.position()].append((equiv_index, "north"))
                            self.equivalence_exit_points[equiv_index].append((tile, "west"))
                        elif tile.type == "\\":
                            self.equivalence_entry_points[tile.position()].append((equiv_index, "south"))
                            self.equivalence_exit_points[equiv_index].append((tile, "west"))

                        finalize_equiv_class()
                        # This tile is the start of the next class
                        tiles_to_cover.insert(0, tile)

            if curr_equiv_class:
                finalize_equiv_class()

        for col in self.tiles_by_col.values():
            curr_equiv_class = []
            tiles_to_cover = [tile for tile in col]

            while tiles_to_cover:
                tile = tiles_to_cover.pop(0)
                curr_equiv_class.append(tile)

                if tile.type in ("|", "-", "/", "\\"):
                    if tile.type == "-":
                        self.equivalence_exit_points[equiv_index].append((tile, "north"))
                        self.equivalence_exit_points[equiv_index].append((tile, "south"))
                    elif tile.type == "|":
                        self.equivalence_entry_points[tile.position()].append((equiv_index, "east"))
                        self.equivalence_entry_points[tile.position()].append((equiv_index, "west"))

                    if len(curr_equiv_class) == 1:
                        if tile.type == "/":
                            self.equivalence_entry_points[tile.position()].append((equiv_index, "east"))
                            self.equivalence_exit_points[equiv_index].append((tile, "south"))
                        elif tile.type == "\\":
                            self.equivalence_entry_points[tile.position()].append((equiv_index, "west"))
                            self.equivalence_exit_points[equiv_index].append((tile, "south"))
                    elif tile.type != "|":
                        if tile.type == "/":
                            self.equivalence_entry_points[tile.position()].append((equiv_index, "west"))
                            self.equivalence_exit_points[equiv_index].append((tile, "north"))
                        elif tile.type == "\\":
                            self.equivalence_entry_points[tile.position()].append((equiv_index, "east"))
                            self.equivalence_exit_points[equiv_index].append((tile, "north"))

                        finalize_equiv_class()
                        # This tile is the start of the next class
                        tiles_to_cover.insert(0, tile)

            if curr_equiv_class:
                finalize_equiv_class()

    def get_energized_locations(self, entry: Position, direction: str) -> Set[Position]:
        start_class = next(cls for cls, direc in self.equivalence_entry_points[entry] if direc == direction)

        equivalence_classes = set()
        classes_to_check = {start_class}

        while classes_to_check:
            curr_equiv_class = classes_to_check.pop()
            equivalence_classes.add(curr_equiv_class)

            for loc, exit_direction in self.equivalence_exit_points[curr_equiv_class]:
                for equiv, entry_direction in self.equivalence_entry_points[loc.position()]:
                    if exit_direction != entry_direction:
                        continue

                    if equiv not in equivalence_classes:
                        classes_to_check.add(equiv)

        energized_locations = {
            loc.position() for eq in equivalence_classes for loc in self.equivalence_classes[eq]
        }

        return energized_locations


def calculate_solution(input_values: InputType) -> int:
    mirrors = MirrorMap(input_values[0])

    locations = mirrors.get_energized_locations((1, 1), "west")

    return len(locations)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
