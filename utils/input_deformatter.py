import re
from typing import Generic, List, Literal, TypeVar, Union

T = TypeVar("T")
X = TypeVar("X")

PrimarySplitEmptyStrategy = Literal["ignore", "sub_split"]
EmptyBoundaryStrategy = Literal["ignore", "strip"]


class InputDeformatter(Generic[T]):
    def __init__(
        self,
        input_primary_split="\n",
        on_empty_primary_split: PrimarySplitEmptyStrategy = "ignore",
        empty_primary_boundary_strategy: EmptyBoundaryStrategy = "strip",
        strip_primary_split=True,
        inline_secondary_split=None,
        empty_secondary_boundary_strategy: EmptyBoundaryStrategy = "ignore",
        strip_secondary_split=False,
        cast_inner_type=None,
    ):
        self._input_primary_split = input_primary_split
        self._on_empty_primary_split = on_empty_primary_split
        self._inline_secondary_split = inline_secondary_split
        self._empty_primary_boundary_strategy = empty_primary_boundary_strategy
        self._empty_secondary_boundary_strategy = empty_secondary_boundary_strategy
        self._cast_inner_type = cast_inner_type
        self._strip_primary_split = strip_primary_split
        self._strip_secondary_split = strip_secondary_split

    def load(self, raw_input: str) -> T:
        if raw_input.strip() == "":
            raise RuntimeError("Input is empty.")

        output_values = []
        current_bucket = output_values

        if self._on_empty_primary_split == "sub_split":
            current_bucket = []
            output_values.append(current_bucket)

        primary_split = self._primary_split(raw_input)

        for entry_idx, primary_entry in enumerate(primary_split):
            if not primary_entry:
                if self._on_empty_primary_split == "sub_split":
                    current_bucket = []
                    output_values.append(current_bucket)

            else:
                line_result = self._secondary_split(primary_entry, entry_idx)

                line_result = self._type_cast(line_result, entry_idx)

                current_bucket.append(line_result)

        if self._input_primary_split is None:
            return output_values[0]

        return output_values

    def _primary_split(self, raw_input: str) -> List[str]:
        if self._input_primary_split is None:
            primary_split = [raw_input]
        elif isinstance(self._input_primary_split, re.Pattern):
            primary_split = re.split(self._input_primary_split, raw_input)
        elif self._input_primary_split:
            primary_split = raw_input.split(self._input_primary_split)
        else:
            primary_split = list(raw_input)

        if self._empty_primary_boundary_strategy == "strip":
            primary_split = self._strip_empty_boundaries(primary_split)

        if self._strip_primary_split:
            primary_split = [primary_entry.strip() for primary_entry in primary_split]

        return primary_split

    @staticmethod
    def _strip_empty_boundaries(value_list: List[str]) -> List[str]:
        if len(value_list) > 0 and not value_list[0]:
            value_list = value_list[1:]

        if len(value_list) > 0 and not value_list[-1]:
            value_list = value_list[:-1]

        return value_list

    def _secondary_split(self, primary_entry: str, entry_idx: int) -> Union[str, List[str]]:
        effective_split = self._get_applicable_from_list(self._inline_secondary_split, entry_idx)

        if effective_split is None:
            return primary_entry

        if effective_split == "":
            inline_split = list(primary_entry)
        else:
            inline_split = primary_entry.split(effective_split)

        if self._strip_secondary_split:
            inline_split = [entry.strip() for entry in inline_split]

        if self._empty_secondary_boundary_strategy == "strip":
            inline_split = self._strip_empty_boundaries(inline_split)

        return inline_split

    def _type_cast(self, entry: Union[str, List[str]], entry_idx: int):
        effective_cast = self._get_applicable_from_list(self._cast_inner_type, entry_idx)

        if effective_cast is None:
            return entry

        if isinstance(entry, list):
            return [effective_cast(val) for val in entry]
        else:
            return effective_cast(entry)

    @staticmethod
    def _get_applicable_from_list(list_like: Union[X, List[X]], entry_idx: int) -> X:
        if isinstance(list_like, list):
            applicable_split_idx = entry_idx % len(list_like)
            return list_like[applicable_split_idx]

        return list_like

    def from_file(self, file_path: str) -> T:
        with open(file_path) as file:
            return self.load(file.read())
