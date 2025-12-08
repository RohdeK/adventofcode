from functools import reduce

from puzzles.day_06.load_inputs import input_reader, InputType


def decolumnize(input_lines: str) -> list[tuple[list[int], str]]:
    actual_lines = input_lines.split("\n")
    actual_lines = [line for line in actual_lines if line]
    max_line = max(len(line) for line in actual_lines)
    actual_lines = [line.ljust(max_line + 1, " ") for line in actual_lines]

    out_vals = []

    iter_vals = []
    iter_op = ""

    for hor_index in range(max_line + 1):
        iter_val = ""

        if all(line[hor_index] == " " for line in actual_lines):
            out_vals.append((iter_vals, iter_op))
            iter_vals = []
            iter_op = ""

        else:
            for idx, line in enumerate(actual_lines[:-1]):
                if line[hor_index] != " ":
                    iter_val += line[hor_index]

            iter_vals.append(iter_val)

            if actual_lines[-1][hor_index] != " ":
                iter_op += actual_lines[-1][hor_index]

    return out_vals


def calculate_solution(input_values: InputType) -> int:
    checksum = 0

    for vals, op in decolumnize(input_values):
        sol = reduce(lambda x, y: eval(f"{x}{op}{y}"), vals)
        checksum += sol

    return checksum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
