from puzzles.day_01.input_part_1 import get_input


def calculate_solution(input_values) -> int:
    calory_sum = [
        sum(per_elf) for per_elf in input_values
    ]

    max_three = sorted(calory_sum, reverse=True)[0:3]

    return sum(max_three)


if __name__ == "__main__":
    print(calculate_solution(get_input()))
