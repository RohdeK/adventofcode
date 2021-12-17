from typing import Tuple

raw_input = """
target area: x=192..251, y=-89..-59
"""


def get_input() -> Tuple[Tuple[int, int], Tuple[int, int]]:
    # Ahem...
    return (192, 251), (-89, -59)
