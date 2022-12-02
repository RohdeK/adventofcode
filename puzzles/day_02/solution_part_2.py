from puzzles.day_02.load_inputs import input_reader, InputType
from puzzles.day_02.solution_part_1 import Move, Round


class StratType:
    def __init__(self, directive: str):
        self._normalized_outcome = {
            "X": -1,
            "Y": 0,
            "Z": 1,
        }[directive]

    def find_move(self, other: Move) -> Move:
        if self._normalized_outcome == -1:
            return other.defeats
        elif self._normalized_outcome == 0:
            return other.draws
        else:
            return other.loses_to


def calculate_solution(input_values: InputType) -> int:
    score = 0

    for opponent_move_raw, strat_type in input_values:
        opponent_move = Move(opponent_move_raw)
        my_move = StratType(strat_type).find_move(opponent_move)
        round_strat = Round(opponent_move, my_move)

        score += round_strat.score

    return score


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
