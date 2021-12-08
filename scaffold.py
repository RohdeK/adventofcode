import os
from pathlib import Path


def scaffold_day(day: int):
    base_path = Path("./puzzles") / f"day_{day}"

    if base_path.is_dir():
        raise ValueError("Day has been set up already.")

    os.makedirs(base_path / "tests")

    (base_path / "solution_part_1.py").write_text(f"""
from puzzles.day_{day}.input_part_1 import get_input

def calculate_solution(input_values) -> int:
    raise NotImplemented

if __name__ == "__main__":
    print(calculate_solution(get_input()))
""")

    (base_path / "solution_part_2.py").write_text(f"""
from puzzles.day_{day}.input_part_1 import get_input

def calculate_solution(input_values) -> int:
    raise NotImplemented

if __name__ == "__main__":
    print(calculate_solution(get_input()))
""")

    (base_path / "input_part_1.py").write_text("""
raw_input = \"\"\"
\"\"\"

def get_input() -> None:
    raise NotImplemented
""")

    (base_path / "tests" / "test_solution_part_1.py").write_text(f"""
from puzzles.day_{day}.solution_part_1 import calculate_solution


def test_example():
    test_input = []

    solution = calculate_solution(test_input)

    assert solution == NotImplemented
""")

    (base_path / "tests" / "test_solution_part_2.py").write_text(f"""
from puzzles.day_{day}.solution_part_2 import calculate_solution


def test_example():
    test_input = []

    solution = calculate_solution(test_input)

    assert solution == NotImplemented
""")


if __name__ == '__main__':
    scaffold_day(8)
