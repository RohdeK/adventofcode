from collections import defaultdict
from typing import Dict, List, Tuple

from puzzles.day_21.input_part_1 import get_input


class PossibilitySpaceDiracGame:
    def __init__(self, starting_pos: Tuple[int, int], max_board_num: int, die_faces: int, win_score: int):
        self.current_state_space: Dict[Tuple[int, int, int, int], int] = defaultdict(int)
        self.current_state_space[(starting_pos[0], starting_pos[1], 0, 0)] = 1

        self.board_size = max_board_num
        self.win_score = win_score

        self.triple_die_result_space: Dict[int, int] = defaultdict(int)
        for i in range(1, die_faces + 1):
            for j in range(1, die_faces + 1):
                for k in range(1, die_faces + 1):
                    self.triple_die_result_space[i + j + k] += 1

        self.player_1_wins = 0
        self.player_2_wins = 0

    def round(self) -> None:
        after_1_positioning: Dict[Tuple[int, int, int, int], int] = defaultdict(int)

        for state, state_frequency in self.current_state_space.items():
            position_1, position_2, score_1, score_2 = state

            for roll, roll_frequency in self.triple_die_result_space.items():

                position_1_after_roll = position_1 + roll
                position_1_after_roll = position_1_after_roll % self.board_size or self.board_size

                score_1_after_roll = score_1 + position_1_after_roll

                after_1_positioning[(position_1_after_roll, position_2, score_1_after_roll, score_2)] += (
                    state_frequency * roll_frequency
                )

        for state, state_frequency in tuple(after_1_positioning.items()):
            _, _, score_1, _ = state

            if score_1 >= self.win_score:
                self.player_1_wins += state_frequency

                del after_1_positioning[state]

        after_2_positioning: Dict[Tuple[int, int, int, int], int] = defaultdict(int)

        for state, state_frequency in after_1_positioning.items():
            position_1, position_2, score_1, score_2 = state

            for roll, roll_frequency in self.triple_die_result_space.items():

                position_2_after_roll = position_2 + roll
                position_2_after_roll = position_2_after_roll % self.board_size or self.board_size

                score_2_after_roll = score_2 + position_2_after_roll

                after_2_positioning[(position_1, position_2_after_roll, score_1, score_2_after_roll)] += (
                    state_frequency * roll_frequency
                )

        for state, state_frequency in tuple(after_2_positioning.items()):
            _, _, _, score_2 = state

            if score_2 >= self.win_score:
                self.player_2_wins += state_frequency

                del after_2_positioning[state]

        self.current_state_space = after_2_positioning

    def play_out(self) -> None:
        while self.current_state_space:
            self.round()


def calculate_solution(input_values: List[int]) -> int:
    game = PossibilitySpaceDiracGame(
        starting_pos=(input_values[0], input_values[1]), max_board_num=10, die_faces=3, win_score=21
    )

    game.play_out()

    return max(game.player_1_wins, game.player_2_wins)


if __name__ == "__main__":
    print(calculate_solution(get_input()))
