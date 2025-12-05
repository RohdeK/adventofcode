from puzzles.day_05.load_inputs import input_reader, InputType


def calculate_solution(input_values: InputType) -> int:
    ranges, _ = input_values
    cut_ranges = []
    iter_ranges = ranges

    while iter_ranges:
        rng = iter_ranges.pop(0)
        next_iter_ranges = []
        cut_ranges.append(rng)

        for irng in iter_ranges:
            if rng.stop <= irng.start:
                # rng is left of irng
                icut = [irng]
            elif rng.start >= irng.stop:
                # rng is right of irng
                icut = [irng]
            elif rng.start >= irng.start and rng.stop - 1 <= irng.stop - 1:
                # rng contained in irng
                icut = [range(irng.start, rng.start), range(rng.stop, irng.stop)]
            elif irng.start >= rng.start and irng.stop - 1 <= rng.stop - 1:
                # irng contained in rng
                icut = []
            elif rng.start <= irng.stop < rng.stop:
                # rng is overlapping irng right
                icut = [range(irng.start, rng.start)]
            elif rng.start < irng.start <= rng.stop - 1:
                # rng is overlapping left
                icut = [range(rng.stop, irng.stop)]
            else:
                raise RuntimeError(rng, irng)

            next_iter_ranges.extend(icut)

        iter_ranges = next_iter_ranges

    return sum(len(rng) for rng in cut_ranges)


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
