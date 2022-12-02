from typing import List

from archive.y2021.puzzles.day_04.input_part_1 import get_input


class BingoBoard:
    def __init__(self, bingo_field: List[List[int]]):
        field_size = len(bingo_field[0])
        assert all(len(row) == field_size for row in bingo_field)

        self._all_numbers = [entry for row in bingo_field for entry in row]
        rows = bingo_field.copy()
        cols = [[row[i] for row in bingo_field] for i in range(field_size)]

        self._win_conditions = rows + cols
        self.bingo = False
        self._last_number = 0

    def cross_number(self, number: int) -> None:
        if self.bingo:
            return

        for line in self._win_conditions + [self._all_numbers]:

            if number in line:
                line.remove(number)

                if len(line) == 0:
                    self.bingo = True
                    self._last_number = number

    def proof_number(self) -> int:
        return sum(self._all_numbers) * self._last_number


def determine_winning_board(boards: List[BingoBoard], draws: List[int]) -> BingoBoard:
    for number in draws:
        for board in boards:
            board.cross_number(number)

            if board.bingo:
                return board

    raise RuntimeError("No board has won.")


if __name__ == "__main__":
    number_draws, bingo_fields = get_input()

    bingo_boards = [BingoBoard(field) for field in bingo_fields]

    winning_board = determine_winning_board(bingo_boards, number_draws)

    print(winning_board.proof_number())
