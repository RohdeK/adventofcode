from puzzles.day_11.load_inputs import input_reader, InputType


def find_ways(ways_dict: dict[str, list[str]]) -> list[list[str]]:
    complete_ways = []
    buildup_ways = [["you"]]

    while buildup_ways:
        iter_ways = []

        for path in buildup_ways:
            curr_position = path[-1]

            if curr_position == "out":
                complete_ways.append(path)
                continue

            next_positions = ways_dict.get(curr_position)

            for next_position in next_positions:
                iter_ways.append(path + [next_position])

        buildup_ways = iter_ways

    return complete_ways


def calculate_solution(input_values: InputType) -> int:
    ways_dict = {
        key[0]: value for key, value in input_values
    }

    ways = find_ways(ways_dict)

    return len(ways)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
