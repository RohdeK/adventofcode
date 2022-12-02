from puzzles.day_01.load_inputs import get_input, InputType


def calculate_solution(input_values: InputType) -> int:
    calory_sum = [
        sum(per_elf) for per_elf in input_values
    ]

    max_three = sorted(calory_sum, reverse=True)[0:3]

    return sum(max_three)


if __name__ == "__main__":
    print(calculate_solution(get_input()))
