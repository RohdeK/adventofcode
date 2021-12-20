from puzzles.day_20.input_part_1 import from_enhancement_line, from_pixel_lines
from puzzles.day_20.solution_part_2 import calculate_solution


def test_example():
    test_pixel_input = [
        "#..#.",
        "#....",
        "##..#",
        "..#..",
        "..###",
    ]

    test_enhancement_input = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"

    test_pixel_field = from_pixel_lines(test_pixel_input)
    test_enhancement = from_enhancement_line(test_enhancement_input)

    solution = calculate_solution(test_pixel_field, test_enhancement)

    assert solution == 3351
