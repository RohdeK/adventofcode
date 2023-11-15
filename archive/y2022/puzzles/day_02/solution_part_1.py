from typing import Union

from archive.y2022.puzzles.day_02.load_inputs import input_reader, InputType


class Move:
    _move_map = {"A": 0, "B": 1, "C": 2}

    def __init__(self, value: Union[str, int]):
        if isinstance(value, str):
            value = self._move_map[value]

        self.value = self._normalize(value)

    @property
    def defeats(self) -> "Move":
        return Move(self.value - 1)

    @property
    def draws(self) -> "Move":
        return Move(self.value)

    @property
    def loses_to(self) -> "Move":
        return Move(self.value + 1)

    @staticmethod
    def _normalize(move_score: int) -> int:
        return move_score % 3

    def __eq__(self, other: "Move") -> bool:
        return self.value == other.value

    def __repr__(self) -> str:
        return {0: "Rock", 1: "Paper", 2: "Scissors"}[self.value]


class Round:
    _move_scorings = {0: 1, 1: 2, 2: 3}
    _win_scorings = {1: 6, 0: 3, -1: 0}

    def __init__(self, opponent_move: Move, my_move: Move):
        self._opponent_move = opponent_move
        self._my_move = my_move

    @property
    def score(self) -> int:
        return self.move_score + self.win_score

    @property
    def move_score(self) -> int:
        return self._move_scorings[self._my_move.value]

    @property
    def win_score(self) -> int:
        return self._win_scorings[self._normalized_win]

    @property
    def _normalized_win(self) -> int:
        if self._my_move.defeats == self._opponent_move:
            return 1
        elif self._my_move.draws == self._opponent_move:
            return 0
        elif self._my_move.loses_to == self._opponent_move:
            return -1


def remap_move(move_desc: str) -> str:
    return {"X": "A", "Y": "B", "Z": "C"}[move_desc]


def calculate_solution(input_values: InputType) -> int:
    score = 0

    for opponent_move, my_move in input_values:
        round_strat = Round(Move(opponent_move), Move(remap_move(my_move)))

        score += round_strat.score

    return score


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
