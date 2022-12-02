from typing import List

from puzzles.day_12.input_part_1 import get_input
from puzzles.day_12.solution_part_1 import PathFinder


class AlteredPathFinder(PathFinder):
    @staticmethod
    def _is_viable_small_cave_rule(node: str, path: List[str]) -> bool:
        has_double_small = any([path.count(node) > 1 for node in path if node.lower() == node])
        if has_double_small:
            # Don't allow revisiting a small cave
            return node not in path
        else:
            return True

    @staticmethod
    def _post_validate_small_cave_rule(path: List[str]) -> None:
        # Doesnt visit any lowercase multiple times, except one 2 times
        small_visit_counts = [path.count(node) for node in path if node.lower() == node]
        assert sum(small_visit_counts) in (len(small_visit_counts), len(small_visit_counts) + 2)


def count_all_paths(input_values: List[str]) -> int:
    finder = AlteredPathFinder(input_values)

    return len(finder.find_all_paths())


if __name__ == "__main__":
    print(count_all_paths(get_input()))
