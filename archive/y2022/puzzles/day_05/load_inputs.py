import re
from typing import List, Tuple

from utils.input_deformatter import InputDeformatter

InputType = Tuple[List[List[str]], List[Tuple[int, int, int]]]


def parse_slots(description: str) -> List[List[str]]:
    heights = description.split("\n")
    heights.reverse()

    slots_def = heights[0]
    slots_indices = [idx for idx, x in enumerate(slots_def) if x != " "]
    slots = [[] for _ in slots_indices]

    for height_row in heights[1:]:
        for slot_index, slot_desc_index in enumerate(slots_indices):
            try:
                slot_content = height_row[slot_desc_index]
            except IndexError:
                continue

            if slot_content != " ":
                slots[slot_index].append(slot_content)

    return slots


def parse_move(description: str) -> Tuple[int, int, int]:
    description, to_slot = description.split(" to ")
    description, from_slot = description.split(" from ")
    _, amount = description.split("move ")

    return int(from_slot), int(to_slot), int(amount)


input_reader = InputDeformatter(
    input_primary_split=re.compile(r"\n\s*\n"),
    inline_secondary_split=[None, "\n"],
    strip_primary_split=False,
    strip_secondary_split=True,
    empty_secondary_boundary_strategy="strip",
    cast_inner_type=[parse_slots, parse_move]
)
