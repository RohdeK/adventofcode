
from puzzles.day_17.load_inputs import input_reader, InputType
from puzzles.day_17.solution_part_1 import RepeatingProducer, Vent


class PeriodicityDetected(Exception):
    def __init__(self, height_shift: int, starting_at_rock: int):
        self.height_shift = height_shift
        self.starting_at_rock = starting_at_rock


class PeriodicVent(Vent):
    def __init__(self, width: int, jetstream: RepeatingProducer[str]):
        super().__init__(width, jetstream)
        self.momoized_situations = {}
        self.fast_forwarded = False

    def cycle_fast_forward(self, num_rocks_settled: int) -> None:
        try:
            while self.rocks_settled < num_rocks_settled:
                self.cycle()
        except PeriodicityDetected as ex:
            self.fast_forwarded = True

            rocks_settled_between = self.rocks_settled - ex.starting_at_rock
            rocks_to_settle = num_rocks_settled - self.rocks_settled
            fast_forward_times = rocks_to_settle // rocks_settled_between
            total_height_shift = fast_forward_times * ex.height_shift

            self.top_positions = [
                y + total_height_shift for y in self.top_positions
            ]
            self.rocks_settled += fast_forward_times * rocks_settled_between

            self.settled_rock_places = [
                (x, y + total_height_shift) for x, y in self.settled_rock_places
            ]

        while self.rocks_settled < num_rocks_settled:
            self.cycle()

    def spawn_rock(self) -> None:
        if not self.fast_forwarded:
            self.check_periodicity()

        super().spawn_rock()

    def check_periodicity(self) -> None:
        current_jetstream_index = self.jetstream.index
        current_rock_producer_index = self.rock_producer.index

        min_memorized_rock = min([y for x, y in self.settled_rock_places], default=0)
        normalized_rocks = [(x, y - min_memorized_rock) for (x, y) in self.settled_rock_places]

        rock_profile = (
            current_jetstream_index,
            current_rock_producer_index,
            ",".join([str(i) for i in normalized_rocks]),
        )

        if rock_profile in self.momoized_situations:
            prev_settled, prev_rockline = self.momoized_situations[rock_profile]
            rock_diffs = [y_new - y_old for (x_new, y_new), (x_old, y_old) in zip(self.settled_rock_places, prev_rockline)]
            assert all(d == rock_diffs[0] for d in rock_diffs)
            raise PeriodicityDetected(rock_diffs[0], prev_settled)
        else:
            self.momoized_situations[rock_profile] = (self.rocks_settled, self.settled_rock_places.copy())


def calculate_solution(input_values: InputType) -> int:
    jetstream = RepeatingProducer(input_values[0])

    vent = PeriodicVent(7, jetstream)

    vent.cycle_fast_forward(1000000000000)

    return vent.highest_position()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
