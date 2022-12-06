import pytest

from puzzles.day_06.load_inputs import input_reader
from puzzles.day_06.solution_part_2 import calculate_solution


@pytest.mark.parametrize(
    ["raw_input", "expected"],
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_example(raw_input, expected):
    test_input = input_reader.load(raw_input)

    solution = calculate_solution(test_input)

    assert solution == expected

