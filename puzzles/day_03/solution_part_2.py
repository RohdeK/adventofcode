
from puzzles.day_03.load_inputs import input_reader, InputType
from puzzles.day_03.solution_part_1 import find_shared_in_sets, score_letter


def calculate_solution(input_values: InputType) -> int:
    score = 0

    for group_index in range(len(input_values) // 3):
        group_sacks = input_values[group_index*3:group_index*3+3]

        commons = find_shared_in_sets(group_sacks)

        score += score_letter(commons)

    return score


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
