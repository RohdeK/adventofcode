from puzzles.day_01.load_inputs import input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    nulltimes = 0
    starting = 50

    for i in input_values:
        rl, dial = i[0], i[1:]
        dial = int(dial)

        residual = dial % 100

        if rl == "L":
            starting -= residual
        else:
            starting += residual

        if starting < 0:
            starting += 100
        elif starting >= 100:
            starting -= 100

        if starting == 0:
            nulltimes += 1

    return nulltimes


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
