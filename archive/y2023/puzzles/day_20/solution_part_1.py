from collections import deque
from enum import Enum
from typing import Deque, Dict, List, Optional, Tuple

from archive.y2023.puzzles.day_20.load_inputs import ModuleConfiguration, input_reader, InputType


class Signal(Enum):
    LOW = 0
    HIGH = 1


class Module:
    def __init__(self, name: str, connected: List[str]):
        self.name = name
        self.connected = connected

    def handle(self, signal: Signal, source: str) -> Optional[Signal]:
        return signal


class FlipFlopModule(Module):
    def __init__(self, conf: ModuleConfiguration):
        if not conf.from_module.startswith("%"):
            raise ValueError(conf)

        self.conf = conf
        super().__init__(conf.from_module[1:], conf.to_modules)

        self.on_state = False

    def handle(self, signal: Signal, _source: str) -> Optional[Signal]:
        if signal == Signal.HIGH:
            return
        elif signal == Signal.LOW:
            self.on_state = not self.on_state

            if self.on_state:
                return Signal.HIGH
            else:
                return Signal.LOW
        else:
            raise ValueError(signal)


class ConjunctionModule(Module):
    def __init__(self, conf: ModuleConfiguration):
        if not conf.from_module.startswith("&"):
            raise ValueError(conf)

        self.conf = conf
        super().__init__(conf.from_module[1:], conf.to_modules)

        self.remembered_states: Dict[str, Signal] = {}

    def handle(self, signal: Signal, source: str) -> Optional[Signal]:
        self.update_state(source, signal)

        if all(s == Signal.HIGH for s in self.remembered_states.values()):
            return Signal.LOW
        else:
            return Signal.HIGH

    def update_state(self, source: str, signal=Signal.LOW) -> None:
        self.remembered_states[source] = signal


class Orchestrator:
    def __init__(self):
        self.command_queue: Deque[Tuple[str, str, Signal]] = deque()
        self.modules: Dict[str, Module] = {}
        self.signals_handled = {
            Signal.LOW: 0,
            Signal.HIGH: 0,
        }
        self.dead_ends = 0

    def add_modules(self, modules: List[ModuleConfiguration]) -> None:
        conjunctions_to_initialize = []

        for conf in modules:
            if conf.from_module.startswith("%"):
                module = FlipFlopModule(conf)
            elif conf.from_module.startswith("&"):
                module = ConjunctionModule(conf)
                conjunctions_to_initialize.append(module.name)
            elif conf.from_module == "broadcaster":
                module = Module(conf.from_module, conf.to_modules)
            else:
                raise ValueError(conf)

            self.modules[module.name] = module

        # Initial states for conjunction modules
        for module in self.modules.values():
            for target in module.connected:
                if target in conjunctions_to_initialize:
                    conj_module = self.modules[target]

                    if not isinstance(conj_module, ConjunctionModule):
                        raise ValueError(conj_module)

                    conj_module.update_state(module.name)

    def handle_signals(self) -> None:
        while len(self.command_queue):
            source, target, signal = self.command_queue.popleft()

            self.signals_handled[signal] += 1

            target_module = self.modules.get(target)

            if target_module is None:
                self.dead_ends += 1
                continue

            next_signal = target_module.handle(signal, source)

            if next_signal is None:
                continue
            else:
                for next_target in target_module.connected:
                    self.command_queue.append((target, next_target, next_signal))

    def press_button(self) -> None:
        self.command_queue.append(("button", "broadcaster", Signal.LOW))
        self.handle_signals()


def calculate_solution(input_values: InputType) -> int:
    orch = Orchestrator()
    orch.add_modules(input_values)

    for i in range(1000):
        orch.press_button()

    return orch.signals_handled[Signal.LOW] * orch.signals_handled[Signal.HIGH]


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
