import itertools
from typing import List, Set, Tuple

from puzzles.day_12.load_inputs import input_reader, InputType


def possible_slots_in_subseg(segment: str, dmg_num: int) -> Set[str]:
    fixed_slots = [idx for idx, s in enumerate(segment) if s == "#"]

    if len(fixed_slots) == 0:
        move_radius = len(segment) - dmg_num + 1
        return {
            "." * x + "#" * dmg_num + "." * (move_radius - x - 1)
            for x in range(move_radius)
        }

    fixed_slots = list(range(min(fixed_slots), max(fixed_slots) + 1))

    if len(fixed_slots) > dmg_num:
        return set()

    if len(fixed_slots) == dmg_num:
        return {segment.replace("?", ".")}

    if len(segment) == dmg_num:
        return {segment.replace("?", "#")}

    qs_to_left = fixed_slots[0]
    qs_to_right = len(segment) - fixed_slots[-1] - 1
    move_radius = dmg_num - len(fixed_slots)

    configurations = set()

    min_right_fill = max(0, move_radius - qs_to_left)

    for to_fill_right in range(min_right_fill, min(move_radius, qs_to_right) + 1):
        to_fill_left = move_radius - to_fill_right

        configurations.add(
            "." * (qs_to_left - to_fill_left)
            + "#" * dmg_num
            + "." * (qs_to_right - to_fill_right)
        )

    return configurations


def possible_segmentations(segment: str, dmgs: List[int]) -> Set[str]:
    if sum(dmgs) + len(dmgs) - 1 > len(segment):
        return set()

    if segment.count("#") > sum(dmgs):
        return set()

    if len(dmgs) == 1:
        return possible_slots_in_subseg(segment, dmgs[0])

    if len(dmgs) == 0:
        return {segment.replace("?", ".")}

    all_segs = set()

    for idx, dmg in enumerate(dmgs):
        segmentation_points = list(range(dmg, len(segment) - sum(dmgs[idx + 1 :])))
        segmentation_points = [s for s in segmentation_points if segment[s] == "?"]

        for segpoint in segmentation_points:
            per_segment_subs = possible_slots_in_subseg(segment[:segpoint], dmg)

            for followup_segs in possible_segmentations(
                segment[segpoint + 1 :], dmgs[idx + 1 :]
            ):
                for init_seg in per_segment_subs:
                    all_segs.add(init_seg + "." + followup_segs)

        # Fucked up, needs to run only once since recursive
        break

    return all_segs


def num_segmentations(seg_desc: str) -> Tuple[int, int]:
    max_split = ""
    dot_next = False

    for char in seg_desc:
        if char == "?":
            max_split += "." if dot_next else "#"
            dot_next = not dot_next
        elif char == "#":
            max_split += char
            dot_next = True
        else:
            raise ValueError(seg_desc)

    max_split_count = len([seg for seg in max_split.split(".") if seg])
    min_split_count = 1 if "#" in seg_desc else 0

    return min_split_count, max_split_count


def possible_dist_count(row_desc: str, dmg_groups: List[int]) -> int:
    dots_at = [idx for idx, char in enumerate(row_desc) if char == "."]
    segments = [seg for seg in row_desc.split(".") if seg]
    subsegs = [num_segmentations(seg) for seg in segments]
    ranges = [list(range(mins, maxs + 1)) for mins, maxs in subsegs]

    possible_allocs = []
    for distro in itertools.product(*ranges):
        if sum(distro) != len(dmg_groups):
            continue

        dmg_distro = []
        iter_helper = 0
        for d in distro:
            dmg_distro.append(dmg_groups[iter_helper : iter_helper + d])
            iter_helper += d

        possible_allocs.append(dmg_distro)

    total_possibilities = set()

    for alloc in possible_allocs:
        alloc_possibilities = {""}
        for seg, subs in zip(segments, alloc):
            follow_up_segs = possible_segmentations(seg, subs)

            alloc_possibilities = {
                stem + follow_up
                for stem, follow_up in itertools.product(
                    alloc_possibilities, follow_up_segs
                )
            }

        total_possibilities = total_possibilities.union(alloc_possibilities)

        assert all(len(t) == sum(len(s) for s in segments) for t in alloc_possibilities)

    total_possibilities_revised = set()

    for t in total_possibilities:
        char_list = list(t)
        for x in dots_at:
            char_list.insert(x, ".")

        assert len(char_list) == len(row_desc)

        total_possibilities_revised.add("".join(char_list))

    return len(total_possibilities_revised)


def calculate_solution(input_values: InputType) -> int:
    check_sum = 0

    for row_desc, dmg_group_dex in input_values:
        dmg_group_dex = [int(d) for d in dmg_group_dex.split(",")]
        check_sum += possible_dist_count(row_desc, dmg_group_dex)

    return check_sum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
