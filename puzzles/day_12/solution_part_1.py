from typing import List, Tuple

from puzzles.day_12.input_part_1 import get_input


class PathFinder:
    def __init__(self, path_strings: List[str]):
        path_split = [path.split("-") for path in path_strings]
        self._paths: List[Tuple[str, str]] = [(start, end) for start, end in path_split]

    def find_all_paths(self) -> List[List[str]]:
        path_buildups: List[List[str]] = [["start"]]
        complete_paths: List[List[str]] = []

        while len(path_buildups):
            buildup_next_iteration: List[List[str]] = []

            for buildup in path_buildups:
                next_nodes = self._find_next_viable_segments(buildup)

                if len(next_nodes) == 0:
                    # Either ended or out of options.
                    if buildup[-1] == "end":
                        complete_paths.append(buildup)
                    continue

                for next_node in next_nodes:
                    buildup_next_iteration.append(buildup + [next_node])

            path_buildups = buildup_next_iteration

        self._post_validate_paths(complete_paths)

        return complete_paths

    def _find_next_viable_segments(self, path: List[str]) -> List[str]:
        if len(path) == 0:
            return ["start"]

        current_node = path[-1]

        if current_node == "end":
            return []

        available_connections = [node for node in self._paths if current_node in node]

        available_targets = [
            (connection[0] if connection[1] == current_node else connection[1]) for connection in available_connections
        ]

        viable_targets = [node for node in available_targets if self._is_viable_pathing(node, path)]

        return viable_targets

    @staticmethod
    def _is_viable_pathing(node: str, path: List[str]) -> bool:
        if node == "start":
            # Don't allow visiting start again
            return False

        if path[-1] == "end":
            # Don't allow going out of end
            return False

        if node == node.lower():
            # Don't allow revisiting a small cave
            return node not in path

        return True

    @staticmethod
    def _post_validate_paths(paths) -> None:
        path_reps: List[str] = []

        for path in paths:
            # Starts in start
            assert path[0] == "start"

            # Ends in end
            assert path[-1] == "end"

            # Doesnt visit any lowercase multiple times (also handles start and end being visited only once)
            assert all(path.count(node) == 1 for node in path if node.lower() == node)

            # Always moves to another node
            assert all(path[i] != path[i + 1] for i in range(len(path) - 1))

            path_reps.append("-".join(path))

        # Didn't count a path twice
        assert len(set(path_reps)) == len(path_reps)


def count_all_paths(input_values: List[str]) -> int:
    finder = PathFinder(input_values)

    return len(finder.find_all_paths())


if __name__ == "__main__":
    print(count_all_paths(get_input()))
