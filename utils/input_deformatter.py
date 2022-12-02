from typing import Generic, Literal, TypeVar

T = TypeVar("T")

PrimarySplitEmptyStrategy = Literal["ignore", "sub_split"]
PrimaryEmptyBoundaryStrategy = Literal["strip"]


class InputDeformatter(Generic[T]):
    def __init__(
        self,
        input_primary_split="\n",
        on_empty_primary_split: PrimarySplitEmptyStrategy = "ignore",
        empty_primary_boundary_strategy: PrimaryEmptyBoundaryStrategy = "strip",
        strip_primary_split=True,
        inline_secondary_split=None,
        cast_inner_type=None,
    ):
        self._input_primary_split = input_primary_split
        self._on_empty_primary_split = on_empty_primary_split
        self._inline_secondary_split = inline_secondary_split
        self._empty_primary_boundary_strategy = empty_primary_boundary_strategy
        self._cast_inner_type = cast_inner_type
        self._strip_primary_split = strip_primary_split

    def load(self, raw_input: str) -> T:
        output_values = []
        current_bucket = output_values

        if self._on_empty_primary_split == "sub_split":
            current_bucket = []
            output_values.append(current_bucket)

        primary_split = raw_input.split(self._input_primary_split)

        if self._empty_primary_boundary_strategy == "strip":
            if len(primary_split) > 0 and not primary_split[0]:
                primary_split = primary_split[1:]

            if len(primary_split) > 0 and not primary_split[-1]:
                primary_split = primary_split[:-1]

        for primary_entry in primary_split:
            if self._strip_primary_split:
                primary_entry = primary_entry.strip()

            if not primary_entry:
                if self._on_empty_primary_split == "sub_split":
                    current_bucket = []
                    output_values.append(current_bucket)

            else:
                line_result = primary_entry

                if self._inline_secondary_split is not None:
                    line_result = primary_entry.split(self._inline_secondary_split)

                if self._cast_inner_type:
                    if isinstance(line_result, list):
                        line_result = [self._cast_inner_type(val) for val in line_result]
                    else:
                        line_result = self._cast_inner_type(line_result)

                current_bucket.append(line_result)

        return output_values

    def from_file(self, file_path: str) -> T:
        with open(file_path) as file:
            return self.load(file.read())
