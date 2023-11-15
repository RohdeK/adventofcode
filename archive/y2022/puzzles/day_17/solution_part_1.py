from typing import Generic, Iterable, List, Sequence, Tuple, TypeVar

from archive.y2022.puzzles.day_17.load_inputs import InputType, input_reader

Position = Tuple[int, int]
T = TypeVar("T")


class RepeatingProducer(Generic[T]):
    def __init__(self, pattern: Sequence[T]):
        self.pattern = pattern
        self.index = -1

    def __next__(self) -> T:
        self.index += 1
        self.index %= len(self.pattern)
        return self.pattern[self.index]


class RockShape:
    def __init__(self, fields: List[Position]):
        self.fields = fields


RowRock = RockShape([(0, 0), (1, 0), (2, 0), (3, 0)])
PlusRock = RockShape([(1, 0), (0, 1), (1, 1), (1, 2), (2, 1)])
AngleRock = RockShape([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)])
ColumnRock = RockShape([(0, 0), (0, 1), (0, 2), (0, 3)])
SquareRock = RockShape([(0, 0), (0, 1), (1, 0), (1, 1)])

RockProducer = RepeatingProducer([
    RowRock,
    PlusRock,
    AngleRock,
    ColumnRock,
    SquareRock,
])


class Rock:
    def __init__(self, shape: RockShape, anchor_position: Position):
        self.shape = shape
        self.anchor_position = anchor_position

    def theorize(self, theoretical_anchor: Position) -> "Rock":
        return Rock(self.shape, theoretical_anchor)

    def __iter__(self) -> Iterable[Position]:
        anchor_x, anchor_y = self.anchor_position
        for field_x, field_y in self.shape.fields:
            yield anchor_x + field_x, anchor_y + field_y


class Vent:
    def __init__(self, width: int, jetstream: RepeatingProducer[str]):
        self.width = width
        self.rock_producer = RockProducer
        self.jetstream = jetstream
        self.current_falling_rock: Rock = None
        self.top_positions = [-1] * width
        self.rocks_settled = 0
        self.settled_rock_places = []
        self.cycles = 0

    def highest_position(self) -> int:
        return max(self.top_positions) + 1

    def spawn_rock(self) -> None:
        next_rock_shape = next(self.rock_producer)
        next_rock_anchor = (2, self.highest_position() + 3)
        self.current_falling_rock = Rock(next_rock_shape, next_rock_anchor)

    def push_rock(self) -> None:
        x_mod = {
            ">": 1,
            "<": -1,
        }[next(self.jetstream)]

        anchor_x, anchor_y = self.current_falling_rock.anchor_position
        self.possibly_move_rock_to((anchor_x + x_mod, anchor_y))

    def fall_rock(self) -> None:
        anchor_x, anchor_y = self.current_falling_rock.anchor_position

        if not self.possibly_move_rock_to((anchor_x, anchor_y - 1)):
            self.settle_rock()

    def settle_rock(self) -> None:
        for position_x, position_y in self.current_falling_rock:
            prev_highest_y = self.top_positions[position_x]

            if position_y > prev_highest_y:
                self.top_positions[position_x] = position_y

            self.settled_rock_places.append((position_x, position_y))

        self.reduce_rock_memory_space()

        self.current_falling_rock = None
        self.rocks_settled += 1

    def reduce_rock_memory_space(self) -> None:
        smallest_y = min(self.top_positions)

        self.settled_rock_places = [
            position for position in self.settled_rock_places if position[1] >= smallest_y
        ]

    def possibly_move_rock_to(self, anchor: Position) -> bool:
        theoretical_rock = self.current_falling_rock.theorize(anchor)

        collides = self.collides(theoretical_rock)

        if not collides:
            self.current_falling_rock.anchor_position = anchor

        return not collides

    def collides(self, rock: Rock) -> bool:
        for position_x, position_y in rock:
            if position_x == -1:
                return True

            if position_x == self.width:
                return True

            if position_y == -1:
                return True

            if (position_x, position_y) in self.settled_rock_places:
                return True

        return False

    def cycle(self) -> None:
        if self.current_falling_rock is None:
            self.spawn_rock()

        self.push_rock()
        self.fall_rock()

        self.cycles += 1


def calculate_solution(input_values: InputType) -> int:
    jetstream = RepeatingProducer(input_values[0])

    vent = Vent(7, jetstream)

    while vent.rocks_settled < 2022:
        vent.cycle()

    return vent.highest_position()


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
