from dataclasses import dataclass
from typing import List, Optional, Tuple

from utils.input_deformatter import InputDeformatter


@dataclass
class Object:
    x: int
    m: int
    a: int
    s: int


@dataclass
class Condition:
    variable: str
    threshold: int

    def apply(self, _o: Object) -> bool:
        raise NotImplemented()


class LargerCondition(Condition):
    def apply(self, o: Object) -> bool:
        return getattr(o, self.variable) > self.threshold

    def __repr__(self):
        return f"{self.variable}>{self.threshold}"


class SmallerCondition(Condition):
    def apply(self, o: Object) -> bool:
        return getattr(o, self.variable) < self.threshold

    def __repr__(self):
        return f"{self.variable}<{self.threshold}"


@dataclass
class Decider:
    then: str
    condition: Optional[Condition]

    def apply(self, o: Object) -> Optional[str]:
        if self.condition is None:
            return self.then
        elif self.condition.apply(o):
            return self.then


@dataclass
class Rule:
    name: str
    deciders: List[Decider]

    def apply(self, o: Object) -> str:
        for decider in self.deciders:
            result = decider.apply(o)
            if result is not None:
                return result

        raise ValueError(o)


InputType = Tuple[List[Rule], List[Object]]


def parse_rule(desc: str) -> Rule:
    deciders = []
    name, desc = desc.strip("}").split("{")
    decider_descs = desc.split(",")
    for desc in decider_descs:
        if ":" in desc:
            condition, then = desc.split(":")
            if ">" in condition:
                variable, threshold = condition.split(">")
                condition = LargerCondition(variable=variable, threshold=int(threshold))
            elif "<" in condition:
                variable, threshold = condition.split("<")
                condition = SmallerCondition(variable=variable, threshold=int(threshold))
            else:
                raise ValueError(condition)
        else:
            then = desc
            condition = None

        deciders.append(Decider(then=then, condition=condition))

    return Rule(name=name, deciders=deciders)


def parse_object(desc: str) -> Object:
    desc = desc.strip("{}")
    x, m, a, s = desc.split(",")
    return Object(
        x=int(x.split("=")[1]),
        m=int(m.split("=")[1]),
        a=int(a.split("=")[1]),
        s=int(s.split("=")[1]),
    )


input_reader = InputDeformatter[InputType](
    input_primary_split="\n\n",
    inline_secondary_split="\n",
    strip_secondary_split=True,
    cast_inner_type=[parse_rule, parse_object]
)
