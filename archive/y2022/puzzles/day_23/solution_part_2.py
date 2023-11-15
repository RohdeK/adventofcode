from archive.y2022.puzzles.day_23.load_inputs import input_reader, InputType
from archive.y2022.puzzles.day_23.solution_part_1 import ElvesDanceMap


class ExtendedElvesDanceMap(ElvesDanceMap):
    def __init__(self, locs):
        super().__init__(locs)
        self.rounds_passed = 0
        self.stopped = False

    def check_finished(self) -> None:
        for elf in self.elves:
            if elf.intended_next_position is not None:
                return

        self.stopped = True

    def run_indefinitely(self) -> None:
        while not self.stopped:
            self.perform_round()
            self.rounds_passed += 1
            self.check_finished()


def calculate_solution(input_values: InputType) -> int:
    elves_map = ExtendedElvesDanceMap(input_values[0])

    elves_map.run_indefinitely()

    return elves_map.rounds_passed


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
