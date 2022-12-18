import os
from pathlib import Path


def scaffold_day(day: int):
    base_path = Path("./puzzles") / f"day_{day:02d}"

    if base_path.is_dir():
        raise ValueError("Day has been set up already.")

    os.makedirs(base_path / "tests")

    (base_path / "solution_part_1.py").write_text(f"""
from puzzles.day_{day:02d}.load_inputs import input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    raise NotImplemented


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
""".lstrip("\n"))

    (base_path / "solution_part_2.py").write_text(f"""
from puzzles.day_{day:02d}.load_inputs import input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    raise NotImplemented


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
""".lstrip("\n"))

    (base_path / "input.txt").touch()

    (base_path / "load_inputs.py").write_text("""
from utils.input_deformatter import InputDeformatter

InputType = None

input_reader = InputDeformatter()
""".lstrip("\n"))

    (base_path / "tests" / "test_solution_part_1.py").write_text(f"""
from puzzles.day_{day:02d}.load_inputs import input_reader
from puzzles.day_{day:02d}.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = \"\"\"
    \"\"\"
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == NotImplemented
""".lstrip("\n"))

    (base_path / "tests" / "test_solution_part_2.py").write_text(f"""
from puzzles.day_{day:02d}.load_inputs import input_reader
from puzzles.day_{day:02d}.solution_part_2 import calculate_solution


def test_example():
    raw_test_input = \"\"\"
    \"\"\"
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == NotImplemented
""".lstrip("\n"))


if __name__ == '__main__':
    days_already_made = os.listdir("./puzzles")
    scaffold_day(len(days_already_made) + 1)
