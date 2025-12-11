from puzzles.day_11.load_inputs import input_reader, InputType


def to_subproblem(
    ways_dict: dict[str, list[str]], to_node: str, avoiding: list[str]
) -> dict[str, list[str]]:
    for avoid in avoiding:
        ways_dict = {key: value for key, value in ways_dict.items() if key != avoid}
        ways_dict = {key: [v for v in value if v != avoid] for key, value in ways_dict.items()}

    while any(len(v) == 0 for k, v in ways_dict.items() if k != to_node):
        keys_to_slash = [
            key for key, value in ways_dict.items() if len(value) == 0 and key != to_node
        ]
        for key in keys_to_slash:
            ways_dict.pop(key)
            for value in ways_dict.values():
                if key in value:
                    value.remove(key)

    return ways_dict


def unravel(
    ways_dict_i: dict[str, list[str]], from_node: str, to_node: str, avoiding: list[str]
) -> int:
    ways_dict_unweighted = to_subproblem(ways_dict_i, to_node, avoiding)

    ways_dict_weighted = {
        key: [(v, 1) for v in value] for key, value in ways_dict_unweighted.items()
    }

    def shrink():
        keys_to_slash = []
        for key, value in ways_dict_weighted.items():
            if len(value) == 1 and value[0][0] == to_node:
                keys_to_slash.append(key)

        for key in keys_to_slash:
            key_weight = ways_dict_weighted.pop(key)[0][1]

            for value in ways_dict_weighted.values():
                match = next((v for v in value if v[0] == key), None)
                if match is not None:
                    value.remove(match)

                    match_to = next((v for v in value if v[0] == to_node), None)

                    if match_to is None:
                        value.append((to_node, match[1] * key_weight))
                    else:
                        value.remove(match_to)
                        value.append((to_node, match[1] * key_weight + match_to[1]))

        return len(keys_to_slash) > 0

    ways_found = 0

    check_next = True
    while check_next:
        if from_node not in ways_dict_weighted:
            break

        if to_node in (v[0] for v in ways_dict_weighted[from_node]):
            way_to = next(v for v in ways_dict_weighted[from_node] if v[0] == to_node)
            ways_found += way_to[1]

            ways_dict_weighted[from_node] = [
                v for v in ways_dict_weighted[from_node] if v[0] != to_node
            ]

            if len(ways_dict_weighted[from_node]) == 0:
                break

        check_next = shrink()

    return ways_found


def calculate_solution(input_values: InputType) -> int:
    ways_dict = {key[0]: value for key, value in input_values}

    svr_dac = unravel(ways_dict, "svr", "dac", ["fft", "out"])
    dac_fft = unravel(ways_dict, "dac", "fft", ["out"])
    fft_out = unravel(ways_dict, "fft", "out", ["dac"])

    svr_fft = unravel(ways_dict, "svr", "fft", ["dac", "out"])
    fft_dac = unravel(ways_dict, "fft", "dac", ["out"])
    dac_out = unravel(ways_dict, "dac", "out", ["fft"])

    ways = svr_dac * dac_fft * fft_out + svr_fft * fft_dac * dac_out

    return ways


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
