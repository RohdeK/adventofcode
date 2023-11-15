import pytest

from archive.y2022.puzzles.day_06.load_inputs import input_reader
from archive.y2022.puzzles.day_06.solution_part_1 import calculate_solution


@pytest.mark.parametrize(
    ["raw_input", "expected"],
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_example(raw_input, expected):
    test_input = input_reader.load(raw_input)

    solution = calculate_solution(test_input)

    assert solution == expected
