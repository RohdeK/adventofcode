import os
from pathlib import Path


def scaffold_day(day: int):
    base_path = Path("./puzzles") / f"day_{day:02d}"

    if base_path.is_dir():
        raise ValueError("Day has been set up already.")

    os.makedirs(base_path / "tests")

    (base_path / "solution_part_1.py").write_text(f"""
from puzzles.day_{day:02d}.load_inputs import get_input, InputType


def calculate_solution(input_values: InputType) -> int:
    raise NotImplemented


if __name__ == "__main__":
    print(calculate_solution(get_input()))
""")

    (base_path / "solution_part_2.py").write_text(f"""
from puzzles.day_{day:02d}.load_inputs import get_input, InputType


def calculate_solution(input_values: InputType) -> int:
    raise NotImplemented


if __name__ == "__main__":
    print(calculate_solution(get_input()))
""")

    (base_path / "input.txt").touch()

    (base_path / "load_inputs.py").write_text("""
InputType = None


def get_raw_input() -> str:
    with open("./input.txt") as file:
        return file.read()


def transform_input(raw_input: str) -> InputType:
    raise NotImplemented()


def get_input() -> InputType:
    return transform_input(get_raw_input())
""")

    (base_path / "tests" / "test_solution_part_1.py").write_text(f"""
from puzzles.day_{day:02d}.load_inputs import transform_input
from puzzles.day_{day:02d}.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = ""
    
    test_input = transform_input(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == NotImplemented
""")

    (base_path / "tests" / "test_solution_part_2.py").write_text(f"""
from puzzles.day_{day:02d}.load_inputs import transform_input
from puzzles.day_{day:02d}.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = ""
    
    test_input = transform_input(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == NotImplemented
""")


if __name__ == '__main__':
    scaffold_day(2)
