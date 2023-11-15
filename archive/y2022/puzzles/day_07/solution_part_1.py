from collections import defaultdict
from typing import Dict, List, Tuple

from archive.y2022.puzzles.day_07.load_inputs import input_reader, InputType


def commands_parser(input_values: InputType) -> List[Tuple[str, int]]:
    files: List[Tuple[str, int]] = []

    current_path = None
    currently_listing = False

    for command_or_output in input_values:
        if command_or_output.startswith("$ cd"):
            currently_listing = False

            _, dirname = command_or_output.split("$ cd ")

            if dirname == "/":
                current_path = ""
            elif dirname == "..":
                current_path = "/".join(current_path.split("/")[:-1])
            else:
                current_path += "/" + dirname

        elif command_or_output.startswith("$ ls"):
            currently_listing = True

        elif currently_listing:
            if command_or_output.startswith("dir"):
                pass
            else:
                filesize, filename = command_or_output.split(" ")
                filepath = current_path + "/" + filename
                files.append((filepath, int(filesize)))

    return files


def list_directories_with_size(files: List[Tuple[str, int]]) -> Dict[str, int]:
    dirs_with_size: Dict[str, int] = defaultdict(int)

    for filepath, filesize in files:
        comps = filepath.split("/")[:-1]

        for idx in range(len(comps)):
            recombined_path = "/".join(comps[:idx + 1])
            if recombined_path == "":
                recombined_path = "/"
            dirs_with_size[recombined_path] += filesize

    return dirs_with_size


def calculate_solution(input_values: InputType) -> int:
    files = commands_parser(input_values)
    dirs = list_directories_with_size(files)

    small_dirs_sizes = [s for s in dirs.values() if s <= 100000]

    return sum(small_dirs_sizes)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
