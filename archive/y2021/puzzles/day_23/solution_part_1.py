from typing import List, Tuple, Dict, Optional
from enum import Enum
import math

from archive.y2021.puzzles.day_23.input_part_1 import get_input


class RoomType(int, Enum):
    Hallway = 0
    Room_1 = 1
    Room_2 = 2
    Room_3 = 3
    Room_4 = 4


class AgentType(str, Enum):
    Amber = "A"
    Bronze = "B"
    Copper = "C"
    Desert = "D"


class Agent:
    def __init__(self, agent_type: AgentType):
        self.type = agent_type
        self.has_been_in_hallway = False

    def desired_room(self) -> RoomType:
        return {
            AgentType.Amber: RoomType.Room_1,
            AgentType.Bronze: RoomType.Room_2,
            AgentType.Copper: RoomType.Room_3,
            AgentType.Desert: RoomType.Room_4,
        }[self.type]


class Slot:
    def __init__(self, agent: Optional[Agent], r_type: RoomType, index: Tuple[int, int]):
        self.occupant = agent
        self.type = r_type
        self.index = index

        self.next_top: Optional[Slot] = None
        self.next_left: Optional[Slot] = None
        self.next_right: Optional[Slot] = None
        self.next_bottom: Optional[Slot] = None

        assert self.type is not None

    def __repr__(self):
        return f"{self.index} ({self.type}) {self.occupant.type if self.occupant else 'free'}"

    def next_free(self) -> List["Slot"]:
        return [
            slot
            for slot in (self.next_right, self.next_left, self.next_top, self.next_bottom)
            if slot and not slot.occupant
        ]


class House:
    def __init__(self, slots: Dict[Tuple[int, int], Slot]):
        self.slots = slots
        self.solving_sum = 0

    @classmethod
    def from_rep(cls, lines: List[str]) -> "House":
        slots_dict: Dict[Tuple[int, int], Slot] = {}

        # "Parsing"
        for i, line in enumerate(lines):
            for j, char in enumerate(list(line)):
                if i == 1:
                    room_type = RoomType.Hallway
                elif j == 3:
                    room_type = RoomType.Room_1
                elif j == 5:
                    room_type = RoomType.Room_2
                elif j == 7:
                    room_type = RoomType.Room_3
                elif j == 9:
                    room_type = RoomType.Room_4
                else:
                    room_type = None

                if char == ".":
                    slots_dict[(j, i)] = Slot(None, room_type, (j, i))
                elif char.upper() in ("A", "B", "C", "D"):
                    if char == char.lower():
                        agent = Agent(char.upper())
                        agent.has_been_in_hallway = True
                    else:
                        agent = Agent(char)

                    slots_dict[(j, i)] = Slot(agent, room_type, (j, i))

        # Interconnections
        for (x, y), slot in slots_dict.items():
            slot.next_left = slots_dict.get((x - 1, y))
            slot.next_right = slots_dict.get((x + 1, y))
            slot.next_top = slots_dict.get((x, y - 1))
            slot.next_bottom = slots_dict.get((x, y + 1))

        return cls(slots_dict)

    def to_rep(self) -> List[str]:
        x_range, y_range = max(dim[0] for dim in self.slots.keys()), max(dim[1] for dim in self.slots.keys())

        target_string_field = [["#" for _ in range(x_range + 2)] for _ in range(y_range + 2)]

        for (i, j), slot in self.slots.items():
            if slot.occupant:
                if slot.occupant.has_been_in_hallway:
                    encoding = slot.occupant.type.lower()
                else:
                    encoding = slot.occupant.type
            else:
                encoding = "."
            target_string_field[j][i] = encoding

        return ["".join(row) for row in target_string_field]

    def copy(self) -> "House":
        copied = House.from_rep(self.to_rep())
        copied.solving_sum = self.solving_sum
        return copied

    def list_possible_moves(self, from_node: Slot) -> List[Slot]:
        if not from_node.occupant:
            raise ValueError("Not moveable")

        target_nodes: List[Slot] = [from_node]

        new_added = True
        while new_added:
            new_added = False

            for node in tuple(target_nodes):
                for next_node in node.next_free():
                    if next_node not in target_nodes:
                        target_nodes.append(next_node)
                        new_added = True

        target_nodes.remove(from_node)

        return [node for node in target_nodes if self.can_move_to(from_node, node)]

    def only_has_valids(self, room_type: RoomType) -> bool:
        for slot in self.slots.values():
            if slot.type == room_type and slot.occupant and room_type != slot.occupant.desired_room():
                return False
        return True

    def can_move_to(self, from_node: Slot, to_node: Slot) -> bool:
        if to_node.type == RoomType.Hallway:
            if to_node.index[1] in (3, 5, 7, 9):
                return False

        if from_node.type == RoomType.Hallway:
            if to_node.type == from_node.occupant.desired_room():
                return self.only_has_valids(from_node.occupant.desired_room())
            else:
                return False

        else:
            if to_node.type == RoomType.Hallway:
                return not from_node.occupant.has_been_in_hallway

            elif to_node.type == from_node.occupant.desired_room():
                return self.only_has_valids(from_node.occupant.desired_room())
            else:
                return False

    def list_all_possible_moves(self) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
        from_to: List[Tuple[Tuple[int, int], Tuple[int, int]]] = []

        for slot in self.slots.values():
            if slot.occupant:
                for next_move in self.list_possible_moves(slot):
                    from_to.append((slot.index, next_move.index))

        return from_to

    def is_solved(self) -> bool:
        for slot in self.slots.values():
            if slot.occupant and slot.type != slot.occupant.desired_room():
                return False

        return True

    def apply_move(self, from_index: Tuple[int, int], to_index: Tuple[int, int]) -> None:
        from_node = self.slots[from_index]
        to_node = self.slots[to_index]

        assert from_node.occupant and not to_node.occupant

        horizontal_move = abs(from_node.index[0] - to_node.index[0])
        if horizontal_move == 0:
            length = abs(from_node.index[1] - to_node.index[1])
        else:
            length = horizontal_move + from_node.index[1] + to_node.index[1]

        self.solving_sum += length * {
            AgentType.Amber: 1,
            AgentType.Bronze: 10,
            AgentType.Copper: 100,
            AgentType.Desert: 1000,
        }[from_node.occupant.type]

        to_node.occupant = from_node.occupant
        from_node.occupant = None

        if to_node.type == RoomType.Hallway:
            to_node.occupant.has_been_in_hallway = True


class MultiHouse:
    def __init__(self, lines: List[str]):
        self.houses = [House.from_rep(lines)]

    def try_all(self) -> int:
        min_solving_sum = math.inf

        while self.houses:
            next_iteration_houses: List[House] = []

            for house in self.houses:
                for move in house.list_all_possible_moves():
                    split_house = house.copy()
                    split_house.apply_move(*move)

                    if split_house.is_solved():
                        if split_house.solving_sum < min_solving_sum:
                            min_solving_sum = split_house.solving_sum
                    elif split_house.solving_sum >= min_solving_sum:
                        continue
                    else:
                        next_iteration_houses.append(split_house)

            self.houses = next_iteration_houses

        return min_solving_sum


def calculate_solution(input_values: List[str]) -> int:
    solver = MultiHouse(input_values)

    return solver.try_all()


if __name__ == "__main__":
    print(calculate_solution(get_input()))
