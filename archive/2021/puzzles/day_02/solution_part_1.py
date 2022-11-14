from typing import List, Tuple

from puzzles.day_02.input_part_1 import get_input


def calculate_course(starting_position: Tuple[int, int], course_description: List[str]) -> Tuple[int, int]:
    horizontal, depth = starting_position

    for command in course_description:
        task, amount = command.split(" ")
        amount = int(amount)

        if task == "forward":
            horizontal += amount

        elif task == "down":
            depth += amount

        elif task == "up":
            depth -= amount

        else:
            print("Wrong input task,", task)

    return horizontal, depth


if __name__ == "__main__":
    final_position = calculate_course((0, 0), course_description=get_input())

    print(final_position)
    print(final_position[0] * final_position[1])
