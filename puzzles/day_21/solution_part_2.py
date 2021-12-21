from typing import List

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
    wins = [0] * len(input_values)
    fac = DieFactory(win_score=21, player_count=len(input_values))

    for die in fac:

        game = DiracGame(starting_pos=input_values, max_board_num=10, win_score=21, die_used=die)

        wins[game.play_out()] += 1

    return max(wins)


if __name__ == "__main__":
    print(calculate_solution(get_input()))
