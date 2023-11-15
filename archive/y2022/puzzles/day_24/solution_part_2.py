from archive.y2022.puzzles.day_24.load_inputs import input_reader, InputType
from archive.y2022.puzzles.day_24.solution_part_1 import BlizzardMap


class ExtendedBlizzardMap(BlizzardMap):
    def run_until_done_and_back(self) -> int:
        self.run_until_done()

        self.possible_states.clear()
        self.possible_states.add(self.target_state)
        self.target_state = (self.min_row, self.starting_col)

        self.run_until_done()

        self.possible_states.clear()
        self.possible_states.add(self.target_state)
        self.target_state = (self.max_row, self.ending_col)

        self.run_until_done()

        return self.time_passed


def calculate_solution(input_values: InputType) -> int:
    bliz = ExtendedBlizzardMap(input_values[0])
    time_passed = bliz.run_until_done_and_back()
    return time_passed


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
