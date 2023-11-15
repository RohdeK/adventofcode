
from archive.y2022.puzzles.day_06.load_inputs import input_reader, InputType


def get_mark(input_values: InputType, mark_size: int) -> int:
    last_four = input_values[:mark_size]

    mark = mark_size

    if len(set(last_four)) == mark_size:
        return mark

    for val in input_values[mark_size:]:
        mark += 1
        last_four.pop(0)
        last_four.append(val)

        if len(set(last_four)) == mark_size:
            return mark


def calculate_solution(input_values: InputType) -> int:
    return get_mark(input_values, 4)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
