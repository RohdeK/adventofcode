from dataclasses import dataclass
from functools import reduce
from typing import Iterable, List

from archive.y2023.puzzles.day_06.load_inputs import input_reader, InputType


@dataclass
class RaceSpec:
    time: int
    distance: int


def win_race(race: RaceSpec) -> List[RaceSpec]:
    winners = []

    for time_held in range(race.time):
        distance_travelled = (race.time - time_held) * time_held

        if distance_travelled > race.distance:
            winners.append(RaceSpec(time=time_held, distance=distance_travelled))

    return winners


def calculate_solution(input_values: InputType) -> int:
    times, distances = input_values
    races = [RaceSpec(time=t, distance=d) for t, d, in zip(times, distances)]

    num_winning_moves = []

    for race in races:
        winning_moves = win_race(race)
        num_winning_moves.append(len(winning_moves))

    return reduce(lambda x, y: x * y, num_winning_moves)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
