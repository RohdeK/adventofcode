from typing import List, Optional


class NumRange:
    def __init__(self, from_: int = None, to_: int = None, range_: int = None):
        if sum(arg is None for arg in (from_, to_, range_)) != 1:
            raise ValueError(f"Need 2 inputs for NumRange, encountered {from_=}, {to_=}, {range_=}")

        self.from_ = from_ if from_ is not None else to_ - range_ + 1
        self.to_ = to_ if to_ is not None else from_ + range_ - 1
        self.range_ = range_ if range_ is not None else self.to_ - self.from_ + 1

        if self.to_ < self.from_:
            raise ValueError(f"Invalid NumRange, encountered {from_=}, {to_=}, {range_=}")

    def __repr__(self):
        return f"[{self.from_}:{self.to_}]"

    def intersect(self, other: "NumRange") -> Optional["NumRange"]:
        if other.to_ < self.from_ or other.from_ > self.to_:
            return None

        return NumRange(
            from_=max(other.from_, self.from_),
            to_=min(other.to_, self.to_),
        )

    def minus(self, other: "NumRange") -> List["NumRange"]:
        remainders = []

        if self.from_ < other.from_:
            remainders.append(
                NumRange(
                    from_=self.from_,
                    to_=min(other.from_ - 1, self.to_)
                )
            )

        if self.to_ > other.to_:
            remainders.append(
                NumRange(
                    from_=max(other.to_ + 1, self.from_),
                    to_=self.to_,
                )
            )

        return remainders
