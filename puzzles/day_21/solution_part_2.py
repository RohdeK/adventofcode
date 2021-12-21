from collections import defaultdict
from typing import Dict, List

from puzzles.day_21.input_part_1 import get_input
from puzzles.day_21.solution_part_1 import DiracGame, Die


class DiracDie(Die):
    def __init__(self, seed: int):
        super().__init__()
        self.profile = f"{seed:3d}"

    def _next_roll_result(self) -> int:
        if self.rolls > len(self.profile):
            return 1

        return int(self.profile[-1]) + 1


class DieFactory:
    def __init__(self, win_score: int, player_count: int):
        self.die_threshold = 3 ** (win_score * player_count * 3)
        self.dies_produced = 0

    def __iter__(self):
        while self.dies_produced < self.die_threshold:
            self.dies_produced += 1

            yield DiracDie(self.dies_produced)


def calculate_solution(input_values: List[int]) -> int:
    die_faces = (1, 2, 3)

    triple_cast = defaultdict(int)
    for i in die_faces:
        for j in die_faces:
            for k in die_faces:
                triple_cast[i + j + k] += 1

    def iterative_roll(
        combination_dict: Dict[int, int],
        previous_rolls: List[int],
        iter_pos: int,
        iter_score: int,
        iter_combinations: int,
    ):
        for triple_roll, combinations in triple_cast.items():

            next_pos = (iter_pos + triple_roll) % 10 or 10
            next_score = iter_score + iter_pos
            next_combinations = iter_combinations * combinations

            if next_score >= 21:
                combination_dict[len(previous_rolls + [triple_roll])] += next_combinations
            else:
                iterative_roll(
                    combination_dict, previous_rolls + [triple_roll], next_pos, next_score, next_combinations
                )

    player_1_combinations_wins = defaultdict(int)
    player_2_combinations_wins = defaultdict(int)

    iterative_roll(player_1_combinations_wins, [], input_values[0], 0, 1)
    iterative_roll(player_2_combinations_wins, [], input_values[1], 0, 1)

    combinations_player_1_wins_over_2 = 0
    combinations_player_2_wins_over_1 = 0

    for roundnr_1, combinations_1 in player_1_combinations_wins.items():
        for roundnr_2, combinations_2 in player_2_combinations_wins.items():
            if roundnr_1 <= roundnr_2:
                combinations_player_1_wins_over_2 += combinations_1 * combinations_2
            else:
                combinations_player_2_wins_over_1 += combinations_1 * combinations_2

    return max(combinations_player_1_wins_over_2, combinations_player_2_wins_over_1)


if __name__ == "__main__":
    print(calculate_solution(get_input()))
