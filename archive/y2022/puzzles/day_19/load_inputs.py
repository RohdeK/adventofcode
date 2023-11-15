import enum
from dataclasses import dataclass
from typing import Dict, List

from utils.input_deformatter import InputDeformatter


class Resource(str, enum.Enum):
    ORE = "ore"
    CLAY = "clay"
    OBSIDIAN = "obsidian"
    GEODE = "geode"


ResourceMap = Dict[Resource, int]


@dataclass
class Blueprint:
    index: int
    ore_robot_cost: ResourceMap
    clay_robot_cost: ResourceMap
    obsidian_robot_cost: ResourceMap
    geode_robot_cost: ResourceMap

    def robots(self) -> Dict[Resource, ResourceMap]:
        return {
           Resource.ORE: self.ore_robot_cost,
           Resource.CLAY: self.clay_robot_cost,
           Resource.OBSIDIAN: self.obsidian_robot_cost,
           Resource.GEODE: self.geode_robot_cost,
        }


def parse_costs(cost_desc: str) -> ResourceMap:
    costs: ResourceMap = {}

    for resources_desc in cost_desc.split(" and "):
        amount, resource = resources_desc.split(" ")

        costs[resource] = int(amount)

    return costs


def parse_blueprint(desc: str) -> Blueprint:
    _, desc = desc.split("Blueprint ")
    blueprint_no, desc = desc.split(": Each ore robot costs ")
    ore_robot_cost_desc, desc = desc.split(". Each clay robot costs ")
    clay_robot_cost_desc, desc = desc.split(". Each obsidian robot costs ")
    obsidian_robot_cost_desc, desc = desc.split(". Each geode robot costs ")
    geode_robot_cost_desc, _ = desc.split(".")

    return Blueprint(
        index=int(blueprint_no),
        ore_robot_cost=parse_costs(ore_robot_cost_desc),
        clay_robot_cost=parse_costs(clay_robot_cost_desc),
        obsidian_robot_cost=parse_costs(obsidian_robot_cost_desc),
        geode_robot_cost=parse_costs(geode_robot_cost_desc),
    )


InputType = List[Blueprint]

input_reader = InputDeformatter(
    cast_inner_type=parse_blueprint
)
