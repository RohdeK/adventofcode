from abc import ABC, abstractmethod
from typing import List, Optional

from puzzles.day_21.input_part_1 import get_input


class Die(ABC):
    def __init__(self):
        self.rolls = 0

    def roll(self) -> int:
        self.rolls += 1
        return self._next_roll_result()

    @abstractmethod
    def _next_roll_result(self) -> int:
        pass


class DeterministicDie(Die):
    def _next_roll_result(self) -> int:
        # Note: Rolls is increased before this method is called.
        return self.rolls % 100 or 100


class DiracGame:
    def __init__(self, starting_pos: List[int], max_board_num: int, die_used: Die, win_score: int):
        self.die = die_used
        self.current_positions = starting_pos
        self.scores = [0] * len(starting_pos)
        self.board_size = max_board_num
        self.win_score = win_score

    def round(self) -> Optional[int]:
        for player_index, player_board_position in enumerate(self.current_positions):
            # Roll 3 times
            roll_result = self.die.roll() + self.die.roll() + self.die.roll()

            # Get new board position wrapped
            player_board_position += roll_result
            player_board_position = player_board_position % self.board_size
            if player_board_position == 0:
                player_board_position = self.board_size

            # Mark position and score
            self.current_positions[player_index] = player_board_position
            self.scores[player_index] += player_board_position

            if self.scores[player_index] >= 1000:
                return player_index

    def play_out(self) -> int:
        for _ in range(self.win_score):
            winner = self.round()

            if winner is not None:
                return winner

        raise RuntimeError(f"Did not get a winner after {self.win_score} rounds.")


def calculate_solution(input_values: List[int]) -> int:
    game = DiracGame(starting_pos=input_values, max_board_num=10, win_score=1000, die_used=DeterministicDie())

    game.play_out()

    return min(game.scores) * game.die.rolls


if __name__ == "__main__":
    print(calculate_solution(get_input()))
