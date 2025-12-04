from typing import List

from archive.y2023.puzzles.day_03.load_inputs import input_reader, InputType


def is_symbol_at(i: int, j: int, values: InputType) -> str:
    if 0 <= i < len(values):
        at_row = values[i]

        if 0 <= j < len(at_row):
            at_cell = at_row[j]

            if at_cell != "." and not at_cell.isdigit():
                return True

    return False


def calculate_solution(input_values: InputType) -> int:
    valid_numbers: List[int] = []

    for row_index, row in enumerate(input_values):

        current_number_rep = ""
        cell_indeces_recorded = []
        number_adj_symbol = False

        for cell_index, cell in enumerate(row):
            if cell.isdigit():
                current_number_rep += cell
                cell_indeces_recorded.append(cell_index)

            if (not cell.isdigit() or cell_index == len(row) - 1) and current_number_rep != "":
                for row_i in (row_index - 1, row_index, row_index + 1):
                    for cell_i in (min(cell_indeces_recorded) - 1, *cell_indeces_recorded, max(cell_indeces_recorded) + 1):
                        if is_symbol_at(row_i, cell_i, input_values):
                            number_adj_symbol = True

                if number_adj_symbol:
                    valid_numbers.append(int(current_number_rep))

                current_number_rep = ""
                cell_indeces_recorded = []
                number_adj_symbol = False

    return sum(valid_numbers)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
