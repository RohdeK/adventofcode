from typing import List

from archive.y2021.puzzles.day_20.input_part_1 import get_input
from archive.y2021.puzzles.day_20.solution_part_1 import enhance_pixels


def calculate_solution(input_pixels: List[List[bool]], input_enhancement: List[bool]) -> int:
    pixel_field = {(x, y): pixel for y, line in enumerate(input_pixels) for x, pixel in enumerate(line)}

    for i in range(50):

        pixel_field = enhance_pixels(pixel_field, input_enhancement, call_even=i % 2 == 1)

    return sum(pixel_field.values())


if __name__ == "__main__":
    enhancement, pixels = get_input()
    print(calculate_solution(pixels, enhancement))
