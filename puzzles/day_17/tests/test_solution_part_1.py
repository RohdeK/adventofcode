from puzzles.day_17.load_inputs import input_reader
from puzzles.day_17.solution_part_1 import calculate_solution


def test_example():
    raw_test_input = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
    """
    
    test_input = input_reader.load(raw_test_input)

    solution = calculate_solution(test_input)

    assert solution == 102
