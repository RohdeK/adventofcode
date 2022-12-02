from statistics import median


from archive.y2021.puzzles.day_07.load_inputs import get_input, InputType


def move_into_line(input_values: InputType) -> int:
    optimal_position = int(median(input_values))

    return sum(abs(pos - optimal_position) for pos in input_values)


if __name__ == "__main__":
    print(move_into_line(get_input()))
