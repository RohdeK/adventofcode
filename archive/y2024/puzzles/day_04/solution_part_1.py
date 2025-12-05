from archive.y2024.puzzles.day_04.load_inputs import input_reader, InputType


def horizontal_search(text: str) -> int:
    return text.count("XMAS") + text.count("SAMX")


def transpose(text: str) -> str:
    transposed = []

    for chars in zip(*text.split("\n")):
        transposed.append("".join(chars))

    return "\n".join(transposed)


def flip(text: str) -> str:
    flipped = []

    for line in transpose(text).split("\n"):
        flipped.append(line[::-1])

    return "\n".join(flipped)


def vertical_search(text: str) -> int:
    return horizontal_search(transpose(text))


def diagonalize(text: str) -> str:
    char_field = {}
    max_lindex = 0
    max_rindex = 0

    for lindex, line in enumerate(text.split("\n")):
        for rindex, char in enumerate(line):
            char_field[(lindex, rindex)] = char
            max_lindex = lindex
            max_rindex = rindex

    skewed = []

    for index_sum in range(max_lindex + max_rindex + 1):
        skew_line = ""

        for rindex in range(index_sum + 1):
            if (index_sum - rindex) > max_lindex:
                continue
            if rindex > max_rindex:
                continue
            skew_line += char_field[(index_sum - rindex, rindex)]

        skewed.append(skew_line)

    return "\n".join(skewed)


def diagonal_clockwise_search(text: str) -> int:
    return horizontal_search(diagonalize(text))


def diagonal_counter_clockwise_search(text: str) -> int:
    return diagonal_clockwise_search(flip(text))


def diagonal_search(text: str) -> int:
    return diagonal_clockwise_search(text) + diagonal_counter_clockwise_search(text)


def calculate_solution(input_values: InputType) -> int:
    occurrences = 0
    occurrences += horizontal_search(input_values)
    occurrences += vertical_search(input_values)
    occurrences += diagonal_search(input_values)

    return occurrences


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
