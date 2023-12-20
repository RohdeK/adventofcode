from dataclasses import dataclass
from typing import List

from utils.input_deformatter import InputDeformatter


@dataclass
class ModuleConfiguration:
    from_module: str
    to_modules: List[str]


InputType = List[ModuleConfiguration]


def cast_module_configuration(desc: str) -> ModuleConfiguration:
    from_module, to_module_desc = desc.split(" -> ")
    to_modules = to_module_desc.split(", ")
    return ModuleConfiguration(from_module=from_module, to_modules=to_modules)


input_reader = InputDeformatter[InputType](
    cast_inner_type=cast_module_configuration,
)
