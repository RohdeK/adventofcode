from typing import Tuple

from archive.y2021.puzzles.day_02.load_inputs import get_input, InputType


def calculate_course(starting_position: Tuple[int, int], course_description: InputType) -> Tuple[int, int]:
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
