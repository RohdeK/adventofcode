import math

from puzzles.day_06.load_inputs import input_reader, InputType
from puzzles.day_06.solution_part_1 import RaceSpec


def num_winning_moves(race: RaceSpec) -> int:
    winning_time_held_min = math.ceil(race.time / 2 - math.sqrt(race.time ** 2 / 4 - race.distance))
    winning_time_held_max = math.floor(race.time / 2 + math.sqrt(race.time ** 2 / 4 - race.distance))

    return winning_time_held_max - winning_time_held_min + 1


def calculate_solution(input_values: InputType) -> int:
    times, distances = input_values
    combined_time = int("".join(str(t) for t in times))
    combined_distance = int("".join(str(d) for d in distances))

    big_race = RaceSpec(time=combined_time, distance=combined_distance)

    return num_winning_moves(big_race)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
