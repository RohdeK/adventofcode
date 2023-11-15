import math
import multiprocessing
from typing import Iterator
from archive.y2022.puzzles.day_19.load_inputs import Blueprint, Resource, ResourceMap, input_reader, InputType


class OutOfTimeException(Exception):
    pass


class InvalidResourceSpentException(Exception):
    pass


class BlueprintRun:
    def __init__(self, blueprint: Blueprint, max_minutes: int):
        self.max_minutes = max_minutes
        self.blueprint = blueprint
        self.resources: ResourceMap = {
            Resource.ORE: 0,
            Resource.CLAY: 0,
            Resource.OBSIDIAN: 0,
            Resource.GEODE: 0,
        }
        self.robots: ResourceMap = {
            Resource.ORE: 1,
            Resource.CLAY: 0,
            Resource.OBSIDIAN: 0,
            Resource.GEODE: 0,
        }
        self.spent_minutes = 0
        self.build_history = {}

        self.needed_for_production = {
            robot_type: max(
                resource_cost.get(robot_type, 0) for resource_cost in self.blueprint.robots().values()
            ) for robot_type in self.blueprint.robots().keys()
        }

    def remaining_time(self) -> int:
        return self.max_minutes - self.spent_minutes

    def geode_potential(self) -> int:
        geodes_at_finish = 0
        geodes_at_finish += self.resources[Resource.GEODE]
        geodes_at_finish += self.robots[Resource.GEODE] * self.remaining_time()
        geodes_at_finish += self.remaining_time() * (self.remaining_time() + 1) // 2
        return geodes_at_finish

    def splice(self) -> "BlueprintRun":
        copied_run = BlueprintRun(self.blueprint, self.max_minutes)
        copied_run.robots = self.robots.copy()
        copied_run.resources = self.resources.copy()
        copied_run.spent_minutes = self.spent_minutes
        copied_run.build_history = self.build_history.copy()
        return copied_run

    def current_production(self) -> ResourceMap:
        return self.robots

    def possible_next_builds(self) -> ResourceMap:
        current_production = self.current_production()
        robots_and_their_production_times: ResourceMap = {}

        for robot_type, robot_cost in self.blueprint.robots().items():
            available_after: ResourceMap = {}

            for resource_type, needed_amount in robot_cost.items():
                if needed_amount == 0:
                    continue

                if current_production[resource_type] == 0:
                    available_after[resource_type] = None
                    break

                remaining_needed_amount = needed_amount - self.resources[resource_type]

                if remaining_needed_amount <= 0:
                    available_after[resource_type] = 0
                    continue

                available_after[resource_type] = math.ceil(remaining_needed_amount / current_production[resource_type])

            if any(v is None for v in available_after.values()):
                continue

            needed_production_time = max(available_after.values())
            robots_and_their_production_times[robot_type] = needed_production_time

        return robots_and_their_production_times

    def viable_next_builds(self) -> ResourceMap:
        current_production = self.current_production()
        robots_and_their_production_times: ResourceMap = {}

        for robot_type, robot_cost in self.blueprint.robots().items():
            if robot_type != Resource.GEODE:
                if self.robots[robot_type] >= self.needed_for_production[robot_type]:
                    continue

            available_after: ResourceMap = {}

            for resource_type, needed_amount in robot_cost.items():
                if needed_amount == 0:
                    continue

                if current_production[resource_type] == 0:
                    available_after[resource_type] = None
                    break

                remaining_needed_amount = needed_amount - self.resources[resource_type]

                if remaining_needed_amount <= 0:
                    available_after[resource_type] = 0
                    continue

                available_after[resource_type] = math.ceil(remaining_needed_amount / current_production[resource_type])

            if any(v is None for v in available_after.values()):
                continue

            needed_production_time = max(available_after.values())
            robots_and_their_production_times[robot_type] = needed_production_time

        return robots_and_their_production_times

    def planned_build(self, robot_type: Resource, affordable_in: int) -> None:
        for _ in range(affordable_in):
            self.harvest()

        self.build(robot_type)

    def harvest(self) -> None:
        for robot_type, robot_count in self.robots.items():
            self.resources[robot_type] += robot_count

        self.progress_time()

    def progress_time(self) -> None:
        self.spent_minutes += 1
        if self.spent_minutes == self.max_minutes:
            raise OutOfTimeException()

    def build(self, robot_type: Resource) -> None:
        self.harvest()

        for resource_type, resource_costs in self.blueprint.robots()[robot_type].items():
            if self.resources[resource_type] < resource_costs:
                raise InvalidResourceSpentException()

            self.resources[resource_type] -= resource_costs

        self.robots[robot_type] += 1
        self.build_history[self.spent_minutes] = robot_type

    def finish(self) -> None:
        while True:
            try:
                self.harvest()
            except OutOfTimeException:
                break


class BlueprintOptimizer:
    def __init__(self, blueprint: Blueprint, max_minutes: int):
        self.max_minutes = max_minutes
        self.blueprint = blueprint
        self.run_most_geodes = 0

    def find_best_run(self) -> BlueprintRun:
        start_run = BlueprintRun(self.blueprint, self.max_minutes)

        for run in self.subdivide_run(start_run):
            if run.resources[Resource.GEODE] > self.run_most_geodes:
                self.run_most_geodes = run.resources[Resource.GEODE]

        return self.run_most_geodes

    def subdivide_run(self, current_run: BlueprintRun) -> Iterator[BlueprintRun]:
        next_builds = current_run.viable_next_builds()

        for robot_type in next_builds.keys():
            iter_run = current_run.splice()

            try:
                iter_run.planned_build(robot_type, next_builds[robot_type])
            except OutOfTimeException:
                yield iter_run
            else:
                if iter_run.geode_potential() > self.run_most_geodes:
                    yield from self.subdivide_run(iter_run)


def get_score(bp: Blueprint) -> int:
    opt = BlueprintOptimizer(bp, 24)
    geodes_found = opt.find_best_run()
    return geodes_found * bp.index


def calculate_solution(input_values: InputType) -> int:
    quality_score = 0

    with multiprocessing.Pool() as p:
        for score in p.imap_unordered(get_score, input_values):
            quality_score += score

    return quality_score


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
