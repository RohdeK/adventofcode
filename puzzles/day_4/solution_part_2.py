from typing import List

from puzzles.day_4.input_part_1 import get_input
from puzzles.day_4.solution_part_1 import BingoBoard


def determine_losing_board(boards: List[BingoBoard], draws: List[int]) -> BingoBoard:
    for number in draws:
        for board in tuple(boards):
            board.cross_number(number)

            if board.bingo:
                if len(boards) == 1:
                    return board
                else:
                    boards.remove(board)

    raise RuntimeError("No board has won.")


if __name__ == "__main__":
    number_draws, bingo_fields = get_input()

    bingo_boards = [BingoBoard(field) for field in bingo_fields]

    losing_board = determine_losing_board(bingo_boards, number_draws)

    print(losing_board.proof_number())
