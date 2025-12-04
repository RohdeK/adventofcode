from datetime import datetime
from typing import List, Tuple
import multiprocessing

from archive.y2023.puzzles.day_12.load_inputs import input_reader, InputType
from archive.y2023.puzzles.day_12.solution_part_1 import possible_dist_count


def sub_solute(sub_set_1: str, sub_set_2: str, dmg_group_dex: List[int]) -> int:
    sub_solution_space = 0

    for i in range(len(dmg_group_dex) + 1):
        dmg_group_1 = dmg_group_dex[:i]
        dmg_group_2 = dmg_group_dex[i:]

        sub_solution_1 = possible_dist_count(sub_set_1, dmg_group_1)
        sub_solution_2 = possible_dist_count(sub_set_2, dmg_group_2)

        sub_solution_space += sub_solution_1 * sub_solution_2

    return sub_solution_space


def split_dist_count(row_desc: str, dmg_group_dex: List[int]) -> int:
    all_dot_indices = [idx for idx, v in enumerate(row_desc) if v == "."]

    if len(all_dot_indices) == 0:
        middle_index = next(
            len(row_desc) // 2 + idx
            for idx, r in enumerate(row_desc[len(row_desc) // 2 :])
            if r == "?"
        )

        iter_type = row_desc[middle_index - 1]
        sequence_length = 0
        while iter_type == "#":
            sequence_length += 1
            iter_type = row_desc[middle_index - sequence_length - 1]

        max_seq = max(dmg_group_dex)

        max_iter_len = max_seq - sequence_length
        sub_num = 0

        for i in range(max_iter_len + 1):
            if row_desc[middle_index + i] == "#":
                continue

            sub_set_1 = row_desc[:middle_index] + "#" * i + "."
            sub_set_2 = row_desc[middle_index + 1 + i :]
            if i == max_iter_len + 1:
                assert sub_solute(sub_set_1, sub_set_2, dmg_group_dex) == 0
            sub_num += sub_solute(sub_set_1, sub_set_2, dmg_group_dex)

        return sub_num
    else:
        middle_distances = [abs(idx - len(row_desc) / 2) for idx in all_dot_indices]
        middle_index = middle_distances.index(min(middle_distances))
        middle_index = all_dot_indices[middle_index]

        sub_set_1 = row_desc[:middle_index]
        sub_set_2 = row_desc[middle_index:]

        return sub_solute(sub_set_1, sub_set_2, dmg_group_dex)


def get_score(input_val: Tuple[str, str]) -> int:
    row_desc, dmg_group_dex = input_val
    row_desc_long = "?".join([row_desc] * 5)
    dmg_group_long = ",".join([dmg_group_dex] * 5)
    dmg_group_long = [int(d) for d in dmg_group_long.split(",")]
    print("Checking", row_desc, dmg_group_dex)
    start = datetime.now()
    dist_count = split_dist_count(row_desc_long, dmg_group_long)
    print("Solved", row_desc, "with", dist_count, "solved in", datetime.now() - start)

    return dist_count


def calculate_solution(input_values: InputType) -> int:
    check_sum = 0

    with multiprocessing.Pool() as p:
        for score in p.imap_unordered(get_score, input_values):
            check_sum += score

    return check_sum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
