import multiprocessing

from puzzles.day_19.load_inputs import Blueprint, input_reader, InputType
from puzzles.day_19.solution_part_1 import BlueprintOptimizer


def get_score(bp: Blueprint) -> int:
    opt = BlueprintOptimizer(bp, 32)
    geodes_found = opt.find_best_run()
    return geodes_found


def calculate_solution(input_values: InputType) -> int:
    quality_score = 1

    with multiprocessing.Pool() as p:
        for score in p.imap_unordered(get_score, input_values[:3]):
            quality_score *= score

    return quality_score


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
