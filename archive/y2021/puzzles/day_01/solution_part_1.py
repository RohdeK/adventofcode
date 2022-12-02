from archive.y2021.puzzles.day_01.load_inputs import get_input, InputType


def count_increases(input_list: InputType) -> int:
    inc = 0

    prev_val = None

    for val in input_list:
        if prev_val is not None:
            if val > prev_val:
                inc += 1

        prev_val = val

    return inc


if __name__ == "__main__":
    print(count_increases(get_input()))
