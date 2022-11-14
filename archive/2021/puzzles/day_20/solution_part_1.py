import math
from collections import defaultdict
from typing import Dict, List, Tuple

from puzzles.day_20.input_part_1 import get_input


def measure_index_field(input_pixels: Dict[Tuple[int, int], bool]) -> Tuple[int, int, int, int]:
    max_x = -math.inf
    max_y = -math.inf
    min_x = math.inf
    min_y = math.inf

    for (x, y) in input_pixels.keys():
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    return min_x, min_y, max_x, max_y


def enhance_pixel_area(input_pixels: Dict[Tuple[int, int], bool], default: bool, cushion_size: int) -> None:
    min_x, min_y, max_x, max_y = measure_index_field(input_pixels)

    # Add default off-values for the lines above and below the field
    for pad in range(1, cushion_size + 1):
        for x in range(min_x - pad, max_x + 1 + pad):
            input_pixels[(x, min_y - pad)] = default
            input_pixels[(x, max_y + pad)] = default

        # Add default off-values for the lines left and right of the field
        for y in range(min_y - pad, max_y + 1 + pad):
            input_pixels[(min_x - pad, y)] = default
            input_pixels[(max_x + pad, y)] = default


def reduce_pixel_area(input_pixels: Dict[Tuple[int, int], bool], cushion_size: int):
    min_x, min_y, max_x, max_y = measure_index_field(input_pixels)

    for pad in range(cushion_size):
        for x in range(min_x + pad, max_x + 1 - pad):
            safe_del(input_pixels, (x, min_y + pad))
            safe_del(input_pixels, (x, max_y - pad))

        # Add default off-values for the lines left and right of the field
        for y in range(min_y + pad, max_y + 1 - pad):
            safe_del(input_pixels, (min_x + pad, y))
            safe_del(input_pixels, (max_x - pad, y))


def safe_del(any_dict: dict, any_key) -> None:
    try:
        del any_dict[any_key]
    except KeyError:
        pass


def enhance_pixels(
    input_pixels: Dict[Tuple[int, int], bool], input_enhancement: List[bool], call_even: bool
) -> Dict[Tuple[int, int], bool]:
    field_safety_cushion = 3
    lookup_field: Dict[Tuple[int, int], int] = defaultdict(int)

    default_pixel = True if (call_even and input_enhancement[0]) else False

    enhance_pixel_area(input_pixels, default_pixel, field_safety_cushion)

    for (x, y), pixel in input_pixels.items():
        # Only do something if pixel was lit
        lookup_field[(x - 1, y - 1)] += int(pixel) * 2 ** 0
        lookup_field[(x + 0, y - 1)] += int(pixel) * 2 ** 1
        lookup_field[(x + 1, y - 1)] += int(pixel) * 2 ** 2
        lookup_field[(x - 1, y + 0)] += int(pixel) * 2 ** 3
        lookup_field[(x + 0, y + 0)] += int(pixel) * 2 ** 4
        lookup_field[(x + 1, y + 0)] += int(pixel) * 2 ** 5
        lookup_field[(x - 1, y + 1)] += int(pixel) * 2 ** 6
        lookup_field[(x + 0, y + 1)] += int(pixel) * 2 ** 7
        lookup_field[(x + 1, y + 1)] += int(pixel) * 2 ** 8

    pixel_field = {(x, y): input_enhancement[lookup_index] for (x, y), lookup_index in lookup_field.items()}

    reduce_pixel_area(pixel_field, field_safety_cushion)

    return pixel_field


def calculate_solution(input_pixels: List[List[bool]], input_enhancement: List[bool]) -> int:
    pixel_field = {(x, y): pixel for y, line in enumerate(input_pixels) for x, pixel in enumerate(line)}

    pixel_field = enhance_pixels(pixel_field, input_enhancement, call_even=False)

    pixel_field = enhance_pixels(pixel_field, input_enhancement, call_even=True)

    return sum(pixel_field.values())


if __name__ == "__main__":
    enhancement, pixels = get_input()
    print(calculate_solution(pixels, enhancement))
