import random
import re
from typing import List

from puzzles.day_15.input_part_1 import get_input


def get_random_paths(width: int, heigth: int, count: int) -> List[str]:
    min_path = "r" * (width - 1) + "d" * (heigth - 1)
    output_paths: List[str] = []

    for _ in range(count):
        shuffled = list(min_path)
        random.shuffle(shuffled)

        output_paths.append("".join(shuffled))

    return output_paths


def wiggle_all(path: str) -> List[str]:
    wiggled_paths: List[str] = []

    for match_obj in re.finditer("dr", path):

        match_from, match_to = match_obj.span()
        wiggled = path[:match_from] + "rd" + path[match_to:]
        wiggled_paths.append(wiggled)

    for match_obj in re.finditer("rd", path):

        match_from, match_to = match_obj.span()
        wiggled = path[:match_from] + "dr" + path[match_to:]
        wiggled_paths.append(wiggled)

    print(f"Wiggled path {path} to {len(wiggled_paths)} variants.")

    return wiggled_paths


def wiggle_optimize(input_values: List[List[int]], path: str) -> List[str]:
    init_len = length(input_values, path)
    current_shortest = [path]
    discarded_variants: List[str] = []
    untested_variants = [path]

    while untested_variants:

        print(f"Got {len(untested_variants)} variants to check.")

        variant_to_check = untested_variants.pop()
        wiggled_variants = wiggle_all(variant_to_check)

        for variant in wiggled_variants:
            if variant in discarded_variants:
                print(f"Variant {variant} already seen and it was not optimal.")
                continue
            if variant in current_shortest:
                print(f"Variant {variant} already seen and it was already shortest.")
                continue

            variant_len = length(input_values, variant)

            if variant_len < init_len:
                untested_variants.append(variant)
                init_len = variant_len
                current_shortest = [variant]
                print(f"Variant {variant} is the new shortest with {variant_len}.")
            elif variant_len == init_len:
                untested_variants.append(variant)
                print(f"Variant {variant} is the another shortest with {variant_len} alongside {current_shortest}.")
                current_shortest.append(variant)
            else:
                print(f"Variant {variant} with len {variant_len} is not better than {init_len}.")
                discarded_variants.append(variant)

    print(f"Returning {len(current_shortest)} wiggle optimized paths with length {init_len}.")

    return current_shortest


def length(input_values: List[List[int]], path: str) -> int:
    total_length = 0
    current_x = 0
    current_y = 0

    for direction in list(path):
        if direction == "d":
            current_y += 1
        elif direction == "u":
            current_y -= 1
        elif direction == "r":
            current_x += 1
        elif direction == "l":
            current_x -= 1
        else:
            raise ValueError(direction)

        total_length += input_values[current_x][current_y]

    return total_length


def shortest_path_length(input_values: List[List[int]]) -> int:
    dims = len(input_values[0]), len(input_values)

    init_paths = get_random_paths(*dims, 1)

    print(f"Got init paths: {init_paths}.")

    better_paths: List[str] = []

    for path in init_paths:
        better_paths.extend(wiggle_optimize(input_values, path))
        print(f"Paths {better_paths} are better than {path}.")

    min_path_len = length(input_values, init_paths[0])

    print(f"Path min starts at {min_path_len}.")

    for path in better_paths:
        if (path_len := length(input_values, path)) < min_path_len:

            print(f"Found better path len with {path_len}.")
            min_path_len = path_len

    return min_path_len


if __name__ == "__main__":
    print(shortest_path_length(get_input()))
